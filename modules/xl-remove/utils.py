import os
from modules.core.utils import setup_directories, extract_excel_file, repackage_excel_file, remove_worksheet_protection, remove_workbook_protection, reset_work
from modules.core.logging_config import configure_module_logger

# Configure logger for xl-remove module
logger = configure_module_logger("xl_remove")

def remove_protections(file_path, base_dir):
    """Remove all workbook and worksheet protections."""
    logger.info(f"Processing file: {os.path.basename(file_path)}")
    dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)
    
    try:
        extract_excel_file(file_path, dir_temp, zip_temp)
        logger.info("File extracted successfully")
        
        # Process worksheets
        worksheets_dir = os.path.join(dir_temp, 'xl', 'worksheets')
        if os.path.exists(worksheets_dir):
            for worksheet_file in os.listdir(worksheets_dir):
                worksheet_path = os.path.join(worksheets_dir, worksheet_file)
                logger.debug(f"Removing protection from worksheet: {worksheet_file}")
                remove_worksheet_protection(worksheet_path, zip_temp, dir_temp)
        
        # Process workbook
        workbook_path = os.path.join(dir_temp, 'xl', 'workbook.xml')
        if os.path.exists(workbook_path):
            logger.debug("Removing protection from workbook.xml")
            remove_workbook_protection(workbook_path, zip_temp, dir_temp)
        
        # Repackage file
        output_filename = 'Unlocked_' + os.path.basename(file_path)
        output_path = os.path.join(dir_unlocked, output_filename)
        repackage_excel_file(zip_temp, output_path, dir_temp)
        logger.info(f"File processed successfully: {output_filename}")
        
        reset_work(zip_temp, dir_temp)
        return output_path
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        reset_work(zip_temp, dir_temp)
        raise e
