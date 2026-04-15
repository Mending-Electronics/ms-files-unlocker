import os
from modules.core.utils import (
    setup_directories, reset_work, extract_excel_file, repackage_excel_file,
    remove_file_from_zip, add_file_to_zip
)


def remove_vba_password(file_path, base_dir):
    """Remove VBA project password by modifying vbaProject.bin."""
    dir_upload, dir_unlocked, dir_temp, zip_temp = setup_directories(base_dir)
    dir_wbook = os.path.join(dir_temp, 'xl')
    
    reset_work(zip_temp, dir_temp)
    
    extract_excel_file(file_path, dir_temp, zip_temp)
    
    # Modify vbaProject.bin to remove password
    vba_project_file = os.path.join(dir_wbook, 'vbaProject.bin')
    
    if os.path.exists(vba_project_file):
        try:
            with open(vba_project_file, 'rb') as f:
                data = bytearray(f.read())
            
            # Replace "DPB=" with "DPx" to remove VBA password
            index = data.find(b'DPB=')
            if index != -1:
                data[index:index+3] = b'DPx'
                
            with open(vba_project_file, 'wb') as f:
                f.write(data)
            
            remove_file_from_zip(zip_temp, 'xl/vbaProject.bin')
            add_file_to_zip(zip_temp, 'xl/', 'vbaProject.bin', dir_temp)
        except Exception as e:
            print(f'vbaProject.bin: No protection detected or error occurred. {str(e)}')
    
    filename = os.path.basename(file_path)
    output_path = os.path.join(dir_unlocked, f"Unlocked_VBA_{filename}")
    
    repackage_excel_file(zip_temp, output_path, dir_temp)
    
    return output_path