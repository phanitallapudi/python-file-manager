
# File Organizer
The File Organizer is a Python script that helps you organize files in a specified source directory by moving them into corresponding destination folders based on their file extensions. This tool can be useful for keeping your files organized and easily accessible.


## Requirements

Before running the script, make sure you have the following:
- Python 3.x
- shutil module (pre-installed with python)
- tkinter module (pre-installed with python)




## How to use
Follow these steps to use the script:
- To use the File Organizer, run the provided Python script in your preferred Python environment.
- Upon running the script, a file dialog will open, prompting you to select the source directory where your unorganized files are located. Choose the directory that contains the files you want to organize and click "Open."
- The script will automatically create destination folders for different file types (e.g., Text Files, Image Files, PDF Files, etc.) in the selected source directory if they don't already exist.
- The script will then iterate through the files in the source directory, determine their file extensions, and move them to the corresponding destination folders based on the file extension-to-folder mapping defined in the script. If a file extension is not explicitly mapped, it will be placed in an "Other Files" folder.
- After organizing all the files, the script will display a message indicating that the file organization process has been completed.

## Customization

You can customize the file extension-to-folder mapping by editing the `extension_to_folder` dictionary in the script. Add or modify entries as needed to suit your specific organizational preferences.

```
extension_to_folder = {
    '.txt': 'Text Files',
    '.jpg': 'Image Files',
    '.jpeg' : 'Image Files',
    '.png' : 'Image Files',
    '.pdf': 'PDF Files',
    '.docx' : 'Word Files',
    '.exe' : 'Executables',
    '.mkv' : 'Video Files'
    # Add more extensions and corresponding folders as needed
}
```
## Disclaimer

This script is provided as-is and without warranties. Always make sure to back up your important files before using any file organization tool to avoid data loss.

## Acknowledgement

Happy downloading! If you encounter any issues or have suggestions for improvements, feel free to [open an issue](https://github.com/phanitallapudi/python-file-manager/issues) or contribute to the project by creating a pull request.