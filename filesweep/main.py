# main.py
# Orchestrates the FileSweep workflow.

def main():
  # 1. Load config
  config = load_config()
  
  # 2. Scan folder
  files = scan_folder(config["target_folder"])
  
  # 3. Rename files
  renamed_files = rename_files(files, config["rename_rules"])
  
  # 4. Sort files
  sorted_files = sort_files(renamed_files(files, config["sort_rules"])
                            
  # 5. Detect duplicates
  duplicates = detect_duplicates(sorted_files)
  
  # 6. Generate report
  generate_report(
    renamed_files=renamed_files,
    sorted_files=sorted_files,
    duplicates=duplicates
  )

# Helper functions (to be implemented later)
def load_config():
  pass

def scan_folder(path):
  # create an empty list to store file paths
  files = []

  # Loop through every item in the folder
  for item in list_items_in_folder(path):
    # If the item is a file, add it to the list
    if is_file(item):
      files.append(item)

    # (Optional future feature)
    # if the item is a folder, you could scan inside it too
    # but for now, FileSweep only scans the top level

  # Return the list of files found
  return files

def rename_files(files, rules):
  # Create an empty list to store renamed file paths
  renamed []

  # Loop through each file in the list
  for file in files:

    # 1. Start with the original filename
    new_name = get_original_filename(file)

    # 2. Apply prefix rule (if enabled)
    if rules["prefix"]:
      new_name = apply_prefix(new_name, rules["prefix'])

    # 3. Apply date formatting rule (if enabled)
    if rules["date_format"]:
    new_name = apply_date_format(new_name, rules["date_format"])

    # 4. Apply category-based naming (optional future feature)
    # Example: "IMG_2024_..." or "DOC_2024_..."
    # For now, just leave this as a placeholder
    # new_name = apply_category_name(new_name)

    #5. Rename the file on disk (actual code later)
    # rename_file_on_disk(file, new_name)

    # 6. Add teh new name to the list
    renamed.append(new_name)

  # Return the list of renamed files
  return renamed

def sort_files(files, rules):
  pass

def detect_duplicates(files):
  pass

def generate_report(**kwargs):
  pass

if __name__ == "__main__":
  main()
