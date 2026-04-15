from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils import remove_vba_password

vba_remove_bp = Blueprint('vba_remove', __name__)


@vba_remove_bp.route('/api/vba-remove', methods=['POST'])
def handle_vba_remove():
    """Handle VBA password removal request."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    base_dir = os.getcwd()
    
    filename = secure_filename(file.filename)
    upload_path = os.path.join(base_dir, 'uploads', filename)
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)
    file.save(upload_path)
    
    try:
        output_path = remove_vba_password(upload_path, base_dir)
        output_filename = os.path.basename(output_path)
        return jsonify({
            'success': True,
            'message': 'VBA password removed successfully',
            'filename': output_filename,
            'note': 'Refer to the ReadMe file to unlock your project after processing'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500