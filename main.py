import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Define the source directory where your files are located
source_directory = filedialog.askdirectory()

# Define the destination directory where you want to organize files

# Create a dictionary to map file extensions to folder names
extension_to_folder = {
    '.txt': 'Text Files',
    '.jpg': 'Image Files',
    '.jpeg' : 'Image Files',
    '.png' : 'Image Files',
    '.pdf': 'PDF Files',
    '.docx' : 'Word Files',
    '.exe' : 'Executables',
    '.mkv' : 'Video Files',
    '.mp4' : 'Video Files'
    # Add more extensions and corresponding folders as needed
}
print("File organization started.")

# Create destination folders if they don't exist
for folder_name in extension_to_folder.values():
    folder_path = os.path.join(source_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    source_filepath = os.path.join(source_directory, filename)

    # Check if the item is a file (not a directory)
    if os.path.isfile(source_filepath):
        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()  # Normalize to lowercase

        # Find the corresponding folder for the extension
        folder_name = extension_to_folder.get(extension, 'Other Files')
        folder_path = os.path.join(source_directory, folder_name)

        # Create the destination folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Create the destination file path
        destination_filepath = os.path.join(folder_path, filename)

        # Move the file to the appropriate folder
        shutil.move(source_filepath, destination_filepath)

print("File organization completed.")
