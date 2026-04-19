from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils import remove_vba_password
from modules.core.logging_config import configure_module_logger

logger = configure_module_logger("vba_remove")

vba_remove_bp = Blueprint('vba_remove', __name__)


@vba_remove_bp.route('/api/vba-remove', methods=['POST'])
def handle_vba_remove():
    """Handle VBA password removal request."""
    logger.info("Received vba-remove request")
    if 'file' not in request.files:
        logger.warning("No file provided in request")
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        logger.warning("No file selected")
        return jsonify({'error': 'No file selected'}), 400
    
    base_dir = os.getcwd()
    
    filename = secure_filename(file.filename)
    upload_path = os.path.join(base_dir, 'upload', filename)
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)
    file.save(upload_path)
    logger.info(f"File saved: {filename}")
    
    try:
        output_path = remove_vba_password(upload_path, base_dir)
        output_filename = os.path.basename(output_path)
        logger.success(f"File processed successfully: {output_filename}")
        return jsonify({
            'success': True,
            'message': 'VBA password removed successfully',
            'filename': output_filename,
            'note': 'Refer to the ReadMe file to unlock your project after processing'
        })
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        return jsonify({'error': str(e)}), 500