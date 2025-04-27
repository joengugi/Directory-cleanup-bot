import os
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(
    description="Clean up directory and put files into folders according to their file types."
)
parser.add_argument(
    "---path",
    type=str,
    default="C:\\Users\\HP 348 G7\\Documents",
    help="Directory path of the file to be cleaned",
)
args = parser.parse_args()
path = args.path

# Check if the specified path exists
if not os.path.exists(path):
    print(f"Error: The directory '{path}' does not exist.")
    exit(1)

print(f"Cleaning up directory: {path}")

# Get all contents in the directory
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, item) for item in dir_content]

# Separate files and folders
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

moved = 0
created_folders = []

print(f"Cleaning up {len(docs)} of {len(dir_content)} elements...")

for doc in docs:
    # Skip hidden files or the script itself
    doc_name = os.path.basename(doc)
    if doc_name.startswith('.') or doc_name == os.path.basename(__file__):
        continue

    # Get the file extension
    _, filetype = os.path.splitext(doc)
    if not filetype:
        continue  # skip files with no extension

    # Folder name based on extension
    subfolder_name = filetype[1:].lower()
    subfolder_path = os.path.join(path, subfolder_name)

    # Create the subfolder if needed
    if subfolder_path not in folders and subfolder_path not in created_folders:
        try:
            os.mkdir(subfolder_path)
            created_folders.append(subfolder_path)
            print(f"Created folder: {subfolder_path}")
        except FileExistsError:
            pass

    # Move the file
    new_doc_path = os.path.join(subfolder_path, doc_name)
    os.rename(doc, new_doc_path)
    moved += 1
    print(f"Moved file: {doc_name} -> {new_doc_path}")

print(f"\nCleanup complete. Total files moved: {moved}")
