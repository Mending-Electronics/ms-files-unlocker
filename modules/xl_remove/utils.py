import os
from modules.core.utils import (
    setup_directories, reset_work, extract_excel_file, repackage_excel_file,
    remove_worksheet_protection, remove_workbook_protection
)


def remove_protections(file_path, base_dir):
    """Remove all workbook and worksheet protections."""
    dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)
    dir_wsheets = os.path.join(dir_temp, 'xl', 'worksheets')
    dir_wbook = os.path.join(dir_temp, 'xl')
    
    reset_work(zip_temp, dir_temp)
    
    extract_excel_file(file_path, dir_temp, zip_temp)
    
    # Remove worksheet protections
    if os.path.exists(dir_wsheets):
        for file in os.listdir(dir_wsheets):
            worksheet = os.path.join(dir_wsheets, file)
            if os.path.isdir(worksheet):
                continue
            remove_worksheet_protection(worksheet, zip_temp, dir_temp)
    
    # Remove workbook protections
    if os.path.exists(dir_wbook):
        for file in os.listdir(dir_wbook):
            workbook = os.path.join(dir_wbook, file)
            if os.path.isdir(workbook):
                continue
            remove_workbook_protection(workbook, zip_temp, dir_temp)
    
    filename = os.path.basename(file_path)
    output_path = os.path.join(dir_unlocked, f"Unlocked_All_{filename}")
    
    repackage_excel_file(zip_temp, output_path, dir_temp)
    
    return output_path