from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils import remove_protections
from modules.core.logging_config import configure_module_logger

logger = configure_module_logger("xl_remove")

xl_remove_bp = Blueprint('xl_remove', __name__)


@xl_remove_bp.route('/api/xl-remove', methods=['POST'])
def handle_xl_remove():
    """Handle Excel protection removal request."""
    logger.info("Received xl-remove request")
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
        output_path = remove_protections(upload_path, base_dir)
        output_filename = os.path.basename(output_path)
        logger.success(f"File processed successfully: {output_filename}")
        return jsonify({
            'success': True,
            'message': 'File processed successfully',
            'filename': output_filename
        })
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        return jsonify({'error': str(e)}), 500