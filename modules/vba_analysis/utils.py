import subprocess
from modules.core.utils import setup_directories, reset_work


def analyze_vba(file_path, base_dir):
    """Analyze VBA code for malware threats using oletools."""
    dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)
    
    reset_work(zip_temp, dir_temp)
    
    try:
        # Use olevba to analyze VBA for malware
        file_path_escaped = file_path.replace('\\', '/')
        
        # Run olevba with reveal and analysis options
        result_reveal = subprocess.run(
            ['olevba', file_path_escaped, '--reveal'],
            capture_output=True,
            text=True
        )
        
        result_analysis = subprocess.run(
            ['olevba', file_path_escaped, '--analysis'],
            capture_output=True,
            text=True
        )
        
        output = {
            'reveal': result_reveal.stdout,
            'analysis': result_analysis.stdout,
            'errors': {
                'reveal': result_reveal.stderr,
                'analysis': result_analysis.stderr
            }
        }
        
        return output
    except Exception as e:
        raise Exception(f'VBA analysis failed: {str(e)}')