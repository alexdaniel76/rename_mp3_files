# GUI PyQt5
import os
import sys
from mutagen.id3 import ID3
from PyQt5 import QtWidgets, QtGui

class RenameWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rename MP3 Files")
        self.setGeometry(100, 100, 500, 200)

        self.init_ui()
        self.init_connections()

    def init_ui(self):
        self.browse_button = QtWidgets.QPushButton("Browse", self)
        self.browse_button.move(20, 20)

        self.rename_button = QtWidgets.QPushButton("Rename", self)
        self.rename_button.move(20, 60)

        self.folder_label = QtWidgets.QLabel("No folder selected", self)
        self.folder_label.move(150, 20)

    def init_connections(self):
        self.browse_button.clicked.connect(self.browse_folder)
        self.rename_button.clicked.connect(self.rename_files)

    def browse_folder(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder", "", options=options)
        if folder:
            self.folder_label.setText(folder)

    def rename_files(self):
        folder = self.folder_label.text()
        if folder == "No folder selected":
            QtWidgets.QMessageBox.warning(self, "Error", "Please select a folder first")
            return

        for filename in os.listdir(folder):
            if filename.endswith(".mp3"):
                filepath = os.path.join(folder, filename)
                audio = ID3(filepath)
                title_1 = audio.get("TRCK", None)
                title_2 = audio.get("TIT2", None)

                if title_2:
                    new_filename = title_1.text[0] + ". " + title_2.text[0] + ".mp3"
                    os.rename(filepath, os.path.join(folder, new_filename))
                else:
                    print(f"Title tag not found for {filename}")

app = QtWidgets.QApplication(sys.argv)
window = RenameWindow()
window.show()
sys.exit(app.exec_())
