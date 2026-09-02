# main.py
# Entry point for the FileSweep application.
#
# Responsibilities:
# - Load configuration settings
# - Coordinate application workflow
# - Call modules in the correct order
#
# Workflow:
# 1. Load configuration
# 2. Scan target folder
# 3. Preview rename actions
# 4. Detect duplicates
# 5. Sort files
# 6. Generate report

import json
from pathlib import Path
from collections import Counter

from modules.scanner import scan_folder
from modules.renamer import rename_files


# Load settings from config.json.
#
# Current Settings:
# - target_folder
# - dry_run
# - rename_rules
#
# Future Settings:
# - sort_rules
# - recursive_scan
# - duplicate_handling
# - logging_options
def load_config():
    """
    Load application settings from config.json.

    Returns:
        dict:
            Configuration values.
    """

    config_path = Path(__file__).parent / "config.json"

    with open(config_path, "r") as file:
        return json.load(file)


def format_size(size_bytes):
    """
    Convert bytes into a human-readable format.

    Args:
        size_bytes (int):
            Size in bytes.

    Returns:
        str:
            Human-readable size.
    """

    for unit in ["B", "KB", "MB", "GB", "TB"]:

        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"

        size_bytes /= 1024

    return f"{size_bytes:.2f} PB"


def main():

    # Load application settings
    config = load_config()

    print("\nConfig Loaded:")
    print("--------------")
    print(config)

    # Scan target folder
    files = scan_folder(
        config["target_folder"]
    )

    # Preview rename operations
    rename_results = rename_files(
        files,
        config["rename_rules"],
        config["dry_run"]
    )

    # Count folders in target directory
    folder_path = Path(
        config["target_folder"]
    )

    folder_count = len([
        item
        for item in folder_path.iterdir()
        if item.is_dir()
    ])

    # Calculate total file size
    total_size = sum(
        file.stat().st_size
        for file in files
    )

    # Display scan summary
    print("\nScan Summary:")
    print("-------------")
    print(f"Target Folder : {config['target_folder']}")
    print(f"Dry Run       : {config['dry_run']}")
    print(f"Files Found   : {len(files)}")
    print(f"Folders Found : {folder_count}")
    print(f"Total Size    : {format_size(total_size)}")
    print(f"Rename Actions: {len(rename_results)}")

    # Analyze file types found during scan
    file_types = []

    for file in files:

        extension = file.suffix.lower()

        if extension:
            file_types.append(extension)
        else:
            file_types.append(
                "[no extension]"
            )

    extension_counts = Counter(
        file_types
    )

    print("\nFile Type Breakdown:")
    print("--------------------")

    for extension, count in sorted(
        extension_counts.items()
    ):
        print(
            f"{extension:<15} {count}"
        )

    # Display discovered files
    #
    # Future Enhancement:
    # - Add file size column
    # - Add last modified date
    # - Export scan results to report
    print("\nFiles Found:")
    print("------------")

    for file in files:
        print(file)


if __name__ == "__main__":
    main()