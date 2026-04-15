import os
import shutil
import zipfile
import lxml.etree as le
import lxml.etree as ET
from lxml import etree


def setup_directories(base_dir):
    """Setup necessary directories for file processing."""
    dir_upload = os.path.join(base_dir, 'uploads')
    dir_unlocked = os.path.join(base_dir, 'unlocked')
    dir_temp = os.path.join(base_dir, '_temp')
    zip_temp = os.path.join(base_dir, '_temp.zip')
    
    os.makedirs(dir_upload, exist_ok=True)
    os.makedirs(dir_unlocked, exist_ok=True)
    
    return dir_upload, dir_unlocked, dir_temp, zip_temp


def cleanup(dir_upload, dir_unlocked, dir_temp, zip_temp):
    """Clean up temporary directories and files."""
    if os.path.exists(zip_temp):
        os.remove(zip_temp)
    if os.path.exists(dir_upload):
        shutil.rmtree(dir_upload)
    if os.path.exists(dir_unlocked):
        shutil.rmtree(dir_unlocked)
    if os.path.exists(dir_temp):
        shutil.rmtree(dir_temp)
    
    os.makedirs(dir_upload, exist_ok=True)
    os.makedirs(dir_unlocked, exist_ok=True)


def reset_work(zip_temp, dir_temp):
    """Reset working directory by removing temporary files."""
    try:
        os.remove(zip_temp)
    except Exception:
        print(f'{zip_temp} is not present in the current directory.')
    
    try:
        shutil.rmtree(dir_temp)
    except Exception:
        print("'_temp' folder is not present in the current directory.")


def extract_excel_file(file_path, temp_dir, zip_temp):
    """Extract Excel file as ZIP to temporary directory."""
    shutil.copyfile(file_path, zip_temp)
    
    with zipfile.ZipFile(zip_temp, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)


def repackage_excel_file(zip_temp, output_path, temp_dir):
    """Repackage Excel file from ZIP and cleanup."""
    if os.path.exists(output_path):
        os.remove(output_path)
    
    os.rename(zip_temp, output_path)
    
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


def remove_file_from_zip(zip_file_path, file_to_remove):
    """Remove a file from ZIP archive."""
    temp_zip_file = zip_file_path + '.temp'
    with zipfile.ZipFile(zip_file_path, 'r') as zip_read:
        with zipfile.ZipFile(temp_zip_file, 'w') as zip_write:
            for item in zip_read.infolist():
                if item.filename != file_to_remove:
                    data = zip_read.read(item.filename)
                    zip_write.writestr(item, data)
    os.remove(zip_file_path)
    os.rename(temp_zip_file, zip_file_path)


def add_file_to_zip(zip_file_path, file_dir, file_to_add, temp_dir):
    """Add a file to ZIP archive."""
    with zipfile.ZipFile(zip_file_path, 'a') as myzip:
        myzip.write(os.path.join(temp_dir, file_to_add), os.path.join(file_dir, file_to_add))


def remove_worksheet_password(worksheet_path, zip_temp, temp_dir):
    """Remove password protection from worksheet XML."""
    try:
        file_in = le.parse(worksheet_path)
        
        # Excel 2007
        for elem in file_in.xpath('//*[attribute::password]'):
            elem.attrib.pop('password')
        
        # Excel 2016
        for elem in file_in.xpath('//*[attribute::algorithmName]'):
            elem.attrib.pop('algorithmName')
        for elem in file_in.xpath('//*[attribute::hashValue]'):
            elem.attrib.pop('hashValue')
        for elem in file_in.xpath('//*[attribute::saltValue]'):
            elem.attrib.pop('saltValue')
        for elem in file_in.xpath('//*[attribute::spinCount]'):
            elem.attrib.pop('spinCount')
        
        xml_head = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>"""
        xml_content_decode = str(le.tostring(file_in).decode())
        xml_content_output = (xml_head + xml_content_decode).encode("utf-8")
        root = etree.fromstring(xml_content_output)
        
        with open(worksheet_path, "wb") as i:
            i.write(etree.tostring(root))
        
        filename = os.path.basename(worksheet_path)
        remove_file_from_zip(zip_temp, f'xl/worksheets/{filename}')
        add_file_to_zip(zip_temp, 'xl/worksheets/', filename, temp_dir)
        
        return True
    except Exception as e:
        print(f'{os.path.basename(worksheet_path)} : No protection detected. {str(e)}')
        return False


def remove_worksheet_protection(worksheet_path, zip_temp, temp_dir):
    """Remove all protection elements from worksheet XML."""
    try:
        tree = ET.parse(worksheet_path)
        root = tree.getroot()
        
        for bad in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheetProtection"):
            bad.getparent().remove(bad)
        
        tree.write(worksheet_path)
        
        filename = os.path.basename(worksheet_path)
        remove_file_from_zip(zip_temp, f'xl/worksheets/{filename}')
        add_file_to_zip(zip_temp, 'xl/worksheets/', filename, temp_dir)
        
        return True
    except Exception as e:
        print(f'{os.path.basename(worksheet_path)} : No protection detected. {str(e)}')
        return False


def remove_workbook_protection(workbook_path, zip_temp, temp_dir):
    """Remove workbook protection from workbook XML."""
    try:
        tree = ET.parse(workbook_path)
        root = tree.getroot()
        
        for bad in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}workbookProtection"):
            bad.getparent().remove(bad)
        
        tree.write(workbook_path)
        
        filename = os.path.basename(workbook_path)
        remove_file_from_zip(zip_temp, f'xl/{filename}')
        add_file_to_zip(zip_temp, 'xl/', filename, temp_dir)
        
        return True
    except Exception as e:
        print(f'{os.path.basename(workbook_path)} : No protection detected. {str(e)}')
        return False