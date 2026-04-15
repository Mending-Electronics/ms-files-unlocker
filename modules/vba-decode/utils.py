import subprocess
from modules.core.logging_config import configure_module_logger

# Configure logger for vba-decode module
logger = configure_module_logger("vba_decode")

def decode_vba(file_path, base_dir):
    """Decode VBA obfuscation using oletools."""
    import os
    logger.info(f"Processing file: {os.path.basename(file_path)}")
    output = {}
    
    try:
        # Deobfuscation
        logger.debug("Running olevba --deobf")
        result = subprocess.run(
            ['olevba', '--deobf', file_path],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.stdout:
            output['deobfuscation'] = result.stdout
            logger.info("Deobfuscation completed")
    except Exception as e:
        logger.error(f'Deobfuscation error: {str(e)}')
    
    try:
        # Decode
        logger.debug("Running olevba --decode")
        result = subprocess.run(
            ['olevba', '--decode', file_path],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.stdout:
            output['decode'] = result.stdout
            logger.info("Decode completed")
    except Exception as e:
        logger.error(f'Decode error: {str(e)}')
    
    try:
        # Reveal
        logger.debug("Running olevba --reveal")
        result = subprocess.run(
            ['olevba', '--reveal', file_path],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.stdout:
            output['reveal'] = result.stdout
            logger.info("Reveal completed")
    except Exception as e:
        logger.error(f'Reveal error: {str(e)}')
    
    logger.info("VBA decoding processing completed")
    return output
