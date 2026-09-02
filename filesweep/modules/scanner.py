# scanner.py
# Scans a target folder and returns a list of files.
#
# Responsibilities:
# - Read contents of target folder
# - Identify files
# - Ignore subfolders (for now)
# - Return file list to main.py
#
# Future Enhancements:
# - Recursive folder scanning
# - File type filtering
# - File age filtering
# - Ignore specific folders/files

from pathlib import Path


def scan_folder(folder_path):
    """
    Scan a folder and return a list of files.

    Args:
        folder_path (str):
            Path to the folder being scanned.

    Returns:
        list:
            List of file paths.
    """

    folder = Path(folder_path)

    files = []

    for item in folder.iterdir():

        if item.is_file():
            files.append(item)

    return files