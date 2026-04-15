from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils import reset_passwords

xl_reset_bp = Blueprint('xl_reset', __name__)


@xl_reset_bp.route('/api/xl-reset', methods=['POST'])
def handle_xl_reset():
    """Handle Excel password reset request."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    base_dir = os.getcwd()
    
    filename = secure_filename(file.filename)
    upload_path = os.path.join(base_dir, 'upload', filename)
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)
    file.save(upload_path)
    
    try:
        output_path = reset_passwords(upload_path, base_dir)
        output_filename = os.path.basename(output_path)
        return jsonify({
            'success': True,
            'message': 'File processed successfully',
            'filename': output_filename
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500