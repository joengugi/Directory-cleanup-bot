import os
import shutil
from tkinter import Tk, Button, Label, filedialog, messagebox

def cleanup_directory(folder_path):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path.")
        return

    moved = 0
    created_folders = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            if ext == "":
                continue

            folder_name = ext[1:].lower()
            dest_folder = os.path.join(folder_path, folder_name)

            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)
                created_folders.append(dest_folder)

            new_path = os.path.join(dest_folder, filename)
            shutil.move(file_path, new_path)
            moved += 1

    messagebox.showinfo("Done", f"Moved {moved} file(s) into folders.")


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        label.config(text=folder)
        cleanup_directory(folder)

# GUI Setup
root = Tk()
root.title("Directory Cleaner")

label = Label(root, text="Select a folder to clean up", width=50)
label.pack(pady=10)

browse_button = Button(root, text="Browse Folder and Clean", command=browse_folder)
browse_button.pack(pady=10)

root.geometry("400x150")
root.mainloop()
