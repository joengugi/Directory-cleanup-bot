# Setting up the Argument Parser
import os 
# Give user control over what folder is cleaned up
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(
    description="Clean up directory and put files into folders according to their file types."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path of the file to be cleaned",
)

# parse the arguments given by the user and extract the path
args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")

# executing script and checking for error

# get all files from given directory
dir_content = os.listdir("C:\\Users\\HP 348 G7\\Downloads")

# create a relative path from the path to the file and the document name
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

# filter our directory content into a documents and folders list
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

# counter to keep track of amount of moved files 
# and list of already created folders to avoid multiple creations
moved = 0
created_folders = []

print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")


# Creating a folder for every file extension
# go through all files and move them into according folders
for doc in docs:
    # separte name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    print(filetype)
    print(full_doc_path)
    print(doc_path)
    print(doc_name)

    break
        # full_doc_path, filetype = os.path.splitext(doc)
        # doc_path = os.path.dirname(full_doc_path)
        # doc_name = os.path.basename(full_doc_path)

        # subfolder_path = os.path.join(path, filetype[1].lower())

        # if subfolder_path not in folders and subfolder_path not in created_folders:
        #      try:
        #           os.mkdir(subfolder_path)
        #           created_folders.append(subfolder_path)
        # print(f"folder already exists at {subfolder_path} created..") except FileExistsError as err:
        # print(f"folder already exists at {subfolder_path}... {err}")

    # skip this file when it is in the directory

    for doc_name in docs:

        filetype = os.path.splitext(doc)

        if doc_name == "directory_clean" or doc_name.startswith('.'):
        # continue
            continue
    # get the subfolder name and create folder if not exist

    # filetype = os.path.splitext(doc)
    subfolder_path = os.path.join(path, filetype[1:].lower())

    if subfolder_path not in folders:
        
        # create the folder

        if subfolder_path not in folders and subfolder_path not in created_folders:
            try:
                os.mkdir(subfolder_path)
                created_folders.append(subfolder_path)
                print(f"Folder {subfolder_path} created.")
            except FileExistsError as err:
                print(f"Folder already exists at {subfolder_path}... {err}")



    if subfolder_path not in folders and subfolder_path not in created_folders:
            try:
                os.mkdir(subfolder_path)
                created_folders.append(subfolder_path)
                print(f"Folder {subfolder_path} created.")
            except FileExistsError as err:
                print(f"Folder already exists at {subfolder_path}... {err}")

# Moving each file into the right subfolder
# get the new folder path and move the file
    new_doc_path = os.path.join(subfolder_path, doc_name) + filetype
    os.rename(doc, new_doc_path)
    moved += 1

    print(f"Moved file {doc} to {new_doc_path}")
    break