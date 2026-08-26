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
  pass

def rename_files(files, rules):
  pass

def sort_files(files, rules):
  pass

def detect_duplicates(files):
  pass

def generate_report(**kwargs):
  pass

if __name__ == "__main__":
  main()
