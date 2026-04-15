from flask import Flask, render_template, send_from_directory
import os

# Import blueprints
from modules.xl_reset import create_blueprint as create_xl_reset_bp
from modules.xl_remove import create_blueprint as create_xl_remove_bp
from modules.vba_remove import create_blueprint as create_vba_remove_bp
from modules.vba_decode import create_blueprint as create_vba_decode_bp
from modules.vba_analysis import create_blueprint as create_vba_analysis_bp
from modules.core.utils import setup_directories, cleanup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Setup directories
base_dir = os.getcwd()
dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)

# Call cleanup at startup
cleanup(dir_upload, dir_unlocked, dir_temp, zip_temp)

# Register blueprints
app.register_blueprint(create_xl_reset_bp())
app.register_blueprint(create_xl_remove_bp())
app.register_blueprint(create_vba_remove_bp())
app.register_blueprint(create_vba_decode_bp())
app.register_blueprint(create_vba_analysis_bp())

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(dir_unlocked, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
