import subprocess
from modules.core.logging_config import configure_module_logger

# Configure logger for vba-analysis module
logger = configure_module_logger("vba_analysis")

def analyze_vba(file_path, base_dir):
    """Analyze VBA code for malware using oletools."""
    import os
    logger.info(f"Processing file: {os.path.basename(file_path)}")
    output = {}
    
    try:
        logger.debug("Running olevba --analysis")
        result = subprocess.run(
            ['olevba', '--analysis', file_path],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.stdout:
            output['analysis'] = result.stdout
            logger.info("VBA analysis completed")
    except Exception as e:
        logger.error(f'Analysis error: {str(e)}')
    
    return output
