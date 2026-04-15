from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils import decode_vba
from modules.core.logging_config import configure_module_logger

logger = configure_module_logger("vba_decode")

vba_decode_bp = Blueprint('vba_decode', __name__)


@vba_decode_bp.route('/api/vba-decode', methods=['POST'])
def handle_vba_decode():
    """Handle VBA decoding request."""
    logger.info("Received vba-decode request")
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
        output = decode_vba(upload_path, base_dir)
        logger.success("VBA decoding completed successfully")
        return jsonify({
            'success': True,
            'message': 'VBA decoding completed',
            'data': output
        })
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        return jsonify({'error': str(e)}), 500
