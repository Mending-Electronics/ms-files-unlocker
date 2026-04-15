import os
from modules.core.utils import setup_directories, remove_file_from_zip, add_file_to_zip, reset_work
from modules.core.logging_config import configure_module_logger

# Configure logger for vba-remove module
logger = configure_module_logger("vba_remove")

def remove_vba_password(file_path, base_dir):
    """Remove VBA project password by modifying vbaProject.bin."""
    logger.info(f"Processing file: {os.path.basename(file_path)}")
    dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)
    
    try:
        import shutil
        import zipfile
        
        # Extract file
        shutil.copyfile(file_path, zip_temp)
        with zipfile.ZipFile(zip_temp, 'r') as zip_ref:
            zip_ref.extractall(dir_temp)
        logger.info("File extracted successfully")
        
        # Modify vbaProject.bin
        vba_path = os.path.join(dir_temp, 'xl', 'vbaProject.bin')
        if os.path.exists(vba_path):
            with open(vba_path, 'rb') as f:
                content = f.read()
            
            # Replace DPB= with DPx=
            content = content.replace(b'DPB=', b'DPx=')
            
            with open(vba_path, 'wb') as f:
                f.write(content)
            logger.info("VBA password removed from vbaProject.bin")
            
            # Update zip
            remove_file_from_zip(zip_temp, 'xl/vbaProject.bin')
            add_file_to_zip(zip_temp, 'xl/', 'vbaProject.bin', dir_temp)
        
        # Repackage file
        output_filename = 'Unlocked_' + os.path.basename(file_path)
        output_path = os.path.join(dir_unlocked, output_filename)
        
        if os.path.exists(output_path):
            os.remove(output_path)
        os.rename(zip_temp, output_path)
        
        if os.path.exists(dir_temp):
            shutil.rmtree(dir_temp)
        
        logger.info(f"File processed successfully: {output_filename}")
        return output_path
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        reset_work(zip_temp, dir_temp)
        raise e
