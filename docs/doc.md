# Tech Documentation for Rename MP3 Files

## Introduction
This codebase provides a PyQt5 GUI for renaming MP3 files in a selected folder. The MP3 files are renamed based on their ID3 metadata tags. The code is structured in such a way that makes it easy to maintain, understand, and extend in the future.

## System Requirements

-   Python 3.x
-   PyQt5
-   Mutagen

## Installation

1.  Install Python 3 if it is not already installed on your system.
2.  Install the required libraries by running the following command in your terminal:
```python
pip install PyQt5 mutagen
```

## Usage

To use the Rename MP3 Files tool, simply run the `rename_mp3_files.py` file. A GUI window will appear with two buttons: "Browse" and "Rename".

1.  Click the "Browse" button to select the folder that contains the MP3 files to be renamed.
2.  After selecting the folder, click the "Rename" button to initiate the renaming process.

The tool renames MP3 files based on the `TRCK` and `TIT2` tags of the MP3 file. If a file does not have both of these tags, the file will not be renamed.


## File Structure
The code consists of a single file named RenameWindow.py which contains the implementation for the GUI.

### Class RenameWindow
This is the main class for the GUI and implements the following:

A browse button that allows the user to select a folder containing MP3 files.
A rename button that renames the MP3 files based on their ID3 metadata tags.
A label that displays the selected folder.
Method init_ui
This method sets up the GUI by creating the browse and rename buttons, and the folder label. It sets the position of each component on the window.

### Method init_connections
This method connects the browse and rename buttons to the corresponding methods.

### Method browse_folder
This method opens a file dialog that allows the user to select a folder. The folder path is then displayed on the folder label.

### Method rename_files
This method retrieves the folder path from the folder label. It then iterates through all the files in the folder, renames MP3 files based on their ID3 metadata tags, and prints a warning message if a title tag is not found for a file.

### Execution
The code is executed by creating an instance of the RenameWindow class and showing the window. The sys.exit call ensures that the program terminates when the window is closed

## Conclusion

The Rename MP3 Files tool is a simple and straightforward tool for renaming MP3 files based on their metadata tags. The tool can be useful for organizing large collections of MP3 files in a consistent and automated manner.
