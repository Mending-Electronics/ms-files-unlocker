from flask import Flask, request, render_template, flash, send_from_directory
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from markupsafe import Markup
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import lxml.etree as le
import lxml.etree as ET
from lxml import etree
import zipfile
import shutil
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

dir = os.getcwd()
dirUpload = os.path.join(dir, 'uploads')
dirUnlocked = os.path.join(dir, 'unlocked')
dirWsheets = os.path.join(dir, '_temp', 'xl', 'worksheets')
dirWbook = os.path.join(dir, '_temp', 'xl')
tempDir = os.path.join(dir, '_temp')
zipTemp = os.path.join(dir, '_temp.zip')

def cleanup():
    if os.path.exists(zipTemp):
        os.remove(zipTemp)
    if os.path.exists(dirUpload):
        shutil.rmtree(dirUpload)
    if os.path.exists(dirUnlocked):
        shutil.rmtree(dirUnlocked)
    os.makedirs(dirUpload, exist_ok=True)
    os.makedirs(dirUnlocked, exist_ok=True)

# Call the cleanup function at startup
cleanup()

class UploadForm(FlaskForm):
    file = FileField('Select Excel file', validators=[FileRequired()])

    unlock_type = RadioField(
        Markup('Select a Process:'),
        choices=[
            ('pass', Markup('<b>Reset Workbook and Worksheets Passwords</b> (Used to keep protection parameters if you need to change lost password)')),
            ('all', Markup('<b>Remove Workbook and Worksheets Protections</b> (If you only need to remove all protections)')),
            ('vba', Markup('<b>Remove VBA Project Password</b> (Note : Refer to the ReadMe file to fix the vba project after the process)')),
            ('decode', Markup('<b>Decodes several common VBA Project Obfuscation</b> (Hex encoding, StrReverse, Base64, VBA expressions)')),
            ('scan', Markup('<b>Cybersecurity Analysis</b> (Find suspicious Malware in the VBA script like Dridex)'))
        ],
        default='pass'
    )

    submit = SubmitField('Start Processing !')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    show_alert = False
    unlocked_filename = None

    # Apply cleanup if file upload field is empty when app starts
    if request.method == 'GET' or not form.file.data:
        cleanup()

    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        uploads_path = os.path.join(dirUpload, filename)
        os.makedirs(os.path.dirname(uploads_path), exist_ok=True)  # Ensure the directory exists
        file.save(uploads_path)
        try:
            unlock_file(filename, form.unlock_type.data)
            flash(f'File {filename} unlocked successfully!', 'success')
            unlocked_filename = "Unlocked_" + filename
        except Exception as e:
            flash(f'Error unlocking file {filename}: {str(e)}', 'danger')
        show_alert = True
    return render_template('index.html', form=form, show_alert=show_alert, unlocked_filename=unlocked_filename)


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(dirUnlocked, filename, as_attachment=True)

def unlock_file(xlFileName, mode):
    xlFileWorkDir = os.path.join(dirUpload, xlFileName)
    xlFileInWork = "_" + xlFileName
    unlocked_file_path = os.path.join(dirUnlocked, "Unlocked_" + xlFileName)

    reset_work()

    shutil.copyfile(xlFileWorkDir, os.path.join(dir, xlFileInWork))
    os.rename(os.path.join(dir, xlFileInWork), zipTemp)

    with zipfile.ZipFile(zipTemp, 'r') as zip_ref:
        zip_ref.extractall(tempDir)

    if mode == "pass":
        remove_protection()
    elif mode == "all":
        remove_protection_all()
    else:
        reset_work()

    if os.path.exists(unlocked_file_path):
        os.remove(unlocked_file_path)
    os.rename(zipTemp, unlocked_file_path)
    shutil.rmtree(tempDir)

def reset_work():
    try:
        os.remove(zipTemp)
    except:
        print(zipTemp + ' is not present in dir.')
    try:
        shutil.rmtree(tempDir)
    except:
        print("'_temp' folder is not present.") 

def remove_protection():
    for file in os.listdir(dirWsheets):
        worksheet = os.path.join(dirWsheets, file)
        if os.path.isdir(worksheet):
            continue
        try:
            fileIn = le.parse(worksheet)
            for elem in fileIn.xpath('//*[attribute::password]'):
                elem.attrib.pop('password')
            xmlHead = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>"""
            xmlContentDecode = str(le.tostring(fileIn).decode())
            xmlContentOutput = (xmlHead + xmlContentDecode).encode("utf-8")
            root = etree.fromstring(xmlContentOutput)
            with open(worksheet, "wb") as i:
                i.write(etree.tostring(root))
            remove_file_from_zip(zipTemp, 'xl/worksheets/' + file)
            add_file_to_zip(zipTemp, 'xl/worksheets/', file)
        except Exception as e:
            print(file + ' : No protection detected. ' + str(e))

def remove_protection_all():
    for file in os.listdir(dirWsheets):
        worksheet = os.path.join(dirWsheets, file)
        if os.path.isdir(worksheet):
            continue
        try:
            tree = ET.parse(worksheet)
            root = tree.getroot()
            for bad in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheetProtection"):
                bad.getparent().remove(bad)
            tree.write(worksheet)
            remove_file_from_zip(zipTemp, 'xl/worksheets/' + file)
            add_file_to_zip(zipTemp, 'xl/worksheets/', file)
        except Exception as e:
            print(file + ' : No protection detected. ' + str(e))
    for file in os.listdir(dirWbook):
        workbook = os.path.join(dirWbook, file)
        if os.path.isdir(workbook):
            continue
        try:
            tree = ET.parse(workbook)
            root = tree.getroot()
            for bad in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}workbookProtection"):
                bad.getparent().remove(bad)
            tree.write(workbook)
            remove_file_from_zip(zipTemp, 'xl/' + file)
            add_file_to_zip(zipTemp, 'xl/', file)
        except Exception as e:
            print(file + ' : No protection detected. ' + str(e))

def remove_file_from_zip(zip_file_path, file_to_remove):
    temp_zip_file = zip_file_path + '.temp'
    with zipfile.ZipFile(zip_file_path, 'r') as zip_read:
        with zipfile.ZipFile(temp_zip_file, 'w') as zip_write:
            for item in zip_read.infolist():
                if item.filename != file_to_remove:
                    data = zip_read.read(item.filename)
                    zip_write.writestr(item, data)
    os.remove(zip_file_path)
    os.rename(temp_zip_file, zip_file_path)

def add_file_to_zip(zip_file_path, fileDir, file_to_add):
    with zipfile.ZipFile(zip_file_path, 'a') as myzip:
        myzip.write(os.path.join(tempDir, file_to_add), os.path.join(fileDir, file_to_add))

if __name__ == "__main__":
    app.run(debug=True)
