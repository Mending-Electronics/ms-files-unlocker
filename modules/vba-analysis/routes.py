from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils import analyze_vba
from modules.core.logging_config import configure_module_logger

logger = configure_module_logger("vba_analysis")

vba_analysis_bp = Blueprint('vba_analysis', __name__)


@vba_analysis_bp.route('/api/vba-analysis', methods=['POST'])
def handle_vba_analysis():
    """Handle VBA analysis request."""
    logger.info("Received vba-analysis request")
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
        output = analyze_vba(upload_path, base_dir)
        logger.success("VBA analysis completed successfully")
        return jsonify({
            'success': True,
            'message': 'VBA analysis completed',
            'data': output
        })
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        return jsonify({'error': str(e)}), 500