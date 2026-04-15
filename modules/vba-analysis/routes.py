from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils import analyze_vba

vba_analysis_bp = Blueprint('vba_analysis', __name__)


@vba_analysis_bp.route('/api/vba-analysis', methods=['POST'])
def handle_vba_analysis():
    """Handle VBA analysis request."""
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
        output = analyze_vba(upload_path, base_dir)
        return jsonify({
            'success': True,
            'message': 'VBA analysis completed',
            'data': output
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500