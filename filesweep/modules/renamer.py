# renamer.py
# Renames files according to configured rules.
#
# Responsibilities:
# - Apply naming rules
# - Generate new file names
# - Support dry-run mode
# - Return rename results
#
# Future Enhancements:
# - Date-based naming
# - Remove invalid characters
# - Category-based naming
# - Collision detection
# - Undo support

from pathlib import Path


def rename_files(files, rules, dry_run=True):
    """
    Rename files according to supplied rules.

    Args:
        files (list):
            Files returned from scanner.

        rules (dict):
            Rename settings from config.

        dry_run (bool):
            If True, only report changes.

    Returns:
        list:
            Rename operations performed
            or planned.
    """

    rename_results = []

    prefix = rules.get("prefix", "")

    print("\nRename Preview:")
    print("---------------")

    for file in files:

        file = Path(file)

        original_name = file.name

        # Start with original name
        new_name = original_name

        # Apply prefix if configured
        if prefix:
            new_name = f"{prefix}_{new_name}"

        # Skip if nothing changed
        if original_name == new_name:
            continue

        new_path = file.with_name(new_name)

        # Record action
        rename_results.append({
            "original": str(file),
            "new": str(new_path)
        })

        if dry_run:

            print(
                f"[DRY RUN] "
                f"{original_name} "
                f"-> "
                f"{new_name}"
            )

        else:

            file.rename(new_path)

            print(
                f"[RENAMED] "
                f"{original_name} "
                f"-> "
                f"{new_name}"
            )

    return rename_results