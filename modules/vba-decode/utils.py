import subprocess
from modules.core.utils import setup_directories, reset_work


def decode_vba(file_path, base_dir):
    """Decode VBA obfuscation using oletools."""
    dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)
    
    reset_work(zip_temp, dir_temp)
    
    try:
        # Use olevba to decode VBA obfuscation
        file_path_escaped = file_path.replace('\\', '/')
        
        # Run olevba with deobfuscation options
        result_deobf = subprocess.run(
            ['olevba', file_path_escaped, '--deobf', '-d'],
            capture_output=True,
            text=True
        )
        
        result_decode = subprocess.run(
            ['olevba', file_path_escaped, '--decode'],
            capture_output=True,
            text=True
        )
        
        result_reveal = subprocess.run(
            ['olevba', file_path_escaped, '--reveal'],
            capture_output=True,
            text=True
        )
        
        output = {
            'deobfuscation': result_deobf.stdout,
            'decode': result_decode.stdout,
            'reveal': result_reveal.stdout,
            'errors': {
                'deobfuscation': result_deobf.stderr,
                'decode': result_decode.stderr,
                'reveal': result_reveal.stderr
            }
        }
        
        return output
    except Exception as e:
        raise Exception(f'VBA decoding failed: {str(e)}')