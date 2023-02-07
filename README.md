# Rename MP3 Files

A Python GUI application for renaming MP3 files. The new name of the file is constructed from the track number and title tags of the file.

## Requirements

-   Python 3.x
-   PyQt5
-   Mutagen

## Installation

```
pip install PyQt5
pip install Mutagen
```

## Usage

To run the application, execute the following command:

```
python rename_mp3_files.py
```

Use the "Browse" button to select the folder containing the MP3 files. Then, click on "Rename" to start the renaming process. The new filenames will be constructed from the track number and title tags of each MP3 file. If a title tag is not found for a file, a message will be printed to the console.

## Limitations

-   The application only works for MP3 files.
-   The new filenames are constructed from the first value of the track number and title tags. If the tag contains multiple values, only the first one will be used.

## Contributing

Contributions are welcome. If you have any suggestions or find any bugs, please open an issue on GitHub.

## License

This project is licensed under the MIT License.
