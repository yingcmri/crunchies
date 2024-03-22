import os
import shutil

def sync_folders(original_folder, target_folder):
    """
    Syncs the target folder with the original folder. If any files are missing in the target folder,
    they are copied from the original folder. The subdirectories are not considered

    :param original_folder: Path to the original folder
    :param target_folder: Path to the target folder
    """
    # Ensure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Get the list of files in both folders, ignoring directories
    original_files = {f for f in os.listdir(original_folder) if os.path.isfile(os.path.join(original_folder, f))}
    target_files = {f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))}

    # Determine the files missing in the target folder
    missing_files = original_files - target_files

    # Copy missing files from the original folder to the target folder
    for file_name in missing_files:
        original_file_path = os.path.join(original_folder, file_name)
        target_file_path = os.path.join(target_folder, file_name)
        shutil.copy2(original_file_path, target_file_path)
        print(f"Copied '{file_name}' to '{target_folder}'")