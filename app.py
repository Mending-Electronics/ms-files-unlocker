from flask import Flask, render_template, send_from_directory
import os
import sys
from loguru import logger

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add script directory to Python path
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# Change to script directory to ensure relative paths work
os.chdir(script_dir)

# Configure loguru for server logs
logs_dir = os.path.join(script_dir, 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Remove default handler
logger.remove()

# Add console handler
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

# Add file handler for server logs
logger.add(
    os.path.join(logs_dir, "server_{time:YYYY-MM-DD}.log"),
    rotation="00:00",
    retention="30 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG"
)

# Import blueprints
from modules.xl_reset import create_blueprint as create_xl_reset_bp
from modules.xl_remove import create_blueprint as create_xl_remove_bp
from modules.vba_remove import create_blueprint as create_vba_remove_bp
from modules.vba_decode import create_blueprint as create_vba_decode_bp
from modules.vba_analysis import create_blueprint as create_vba_analysis_bp
from modules.core.utils import setup_directories, cleanup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

logger.info("Starting MS Files Unlocker application")

# Setup directories
base_dir = script_dir
dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)
logger.info(f"Directories setup: upload={dir_upload}, output={dir_unlocked}")

# Call cleanup at startup
cleanup(dir_upload, dir_unlocked, dir_temp, zip_temp)
logger.info("Cleanup completed at startup")

# Register blueprints
app.register_blueprint(create_xl_reset_bp())
app.register_blueprint(create_xl_remove_bp())
app.register_blueprint(create_vba_remove_bp())
app.register_blueprint(create_vba_decode_bp())
app.register_blueprint(create_vba_analysis_bp())
logger.info("All blueprints registered successfully")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(dir_unlocked, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
