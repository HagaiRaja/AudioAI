# This Python file uses the following encoding: utf-8
import sys, os, time

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QFrame, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtGui import (QFont)
from PySide6.QtCore import (QRect, QSize, QCoreApplication)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Main

class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.refresh_recordings()
        self.root_dir = "./sounds/"
        self.recordings = []
        self.load_files()
        self.ui.menu_settings_button.clicked.connect(self.selectDirectoryDialog)

    def refresh_recordings(self):
        self.ui.recording_container_content = QWidget()
        self.ui.recording_container_content.setObjectName(u"recording_container_content")
        self.ui.recording_container_content.setGeometry(QRect(0, 0, 174, 397))
        self.ui.recording_container_layout = QVBoxLayout(self.ui.recording_container_content)
        self.ui.recording_container_layout.setObjectName(u"recording_container_layout")
        self.ui.recording_container_scrollArea.setWidget(self.ui.recording_container_content)

    def selectDirectoryDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Root Directory")
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        if file_dialog.exec():
            selected_directory = file_dialog.selectedFiles()[0]
            if self.root_dir != selected_directory:
                self.root_dir = selected_directory
                self.load_files()

    def load_files(self):
        files = [] # contains pair of (relative path to root_dir, created_at)
        for root, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                # only include audio files
                if not filename.endswith((".wav", ".mp3", ".ogg", ".m4a")): continue
                filepath = os.path.relpath(os.path.join(root, filename), self.root_dir)
                created_at = os.path.getctime(os.path.join(root, filename))
                # convert created_at to human readable format e.g. Mon, 2021-09-01 12:00
                created_at = time.strftime("%a, %Y-%m-%d %H:%M", time.localtime(created_at))
                files.append((filepath, created_at))
                print(files[-1])
        
        # sort files by created_at from newest to oldest
        files.sort(key=lambda x: x[1], reverse=True)
        
        # render files to list widget
        self.refresh_recordings()
        for id, file in enumerate(files):
            filepath, created_at = file
            # add item to widget
            recording_frame = QFrame()
            recording_frame.setObjectName(f"recording{id}_frame")
            recording_frame.setMaximumSize(QSize(16777215, 70))
            recording_frame.setFrameShape(QFrame.StyledPanel)
            recording_frame.setFrameShadow(QFrame.Raised)
            verticalLayout = QVBoxLayout(recording_frame)
            verticalLayout.setSpacing(0)
            verticalLayout.setObjectName(f"verticalLayout_{id}")
            verticalLayout.setContentsMargins(5, 0, 0, 0)

            recording_title = QLabel(recording_frame)
            recording_title.setObjectName(f"recording{id}_title")
            font2 = QFont()
            font2.setFamilies([u"Poppins"])
            font2.setBold(True)
            recording_title.setFont(font2)
            recording_title.setStyleSheet(u"color: #333;")
            verticalLayout.addWidget(recording_title)
            recording_title.setText(QCoreApplication.translate("Main", filepath, None))

            recording_datetime = QLabel(recording_frame)
            recording_datetime.setObjectName(f"recording{id}_datetime")
            font3 = QFont()
            font3.setFamilies([u"Poppins"])
            font3.setItalic(False)
            recording_datetime.setFont(font3)
            recording_datetime.setStyleSheet(u"color: #858585;")
            verticalLayout.addWidget(recording_datetime)
            recording_datetime.setText(QCoreApplication.translate("Main", created_at, None))

            # Add to layout and storage
            self.ui.recording_container_layout.addWidget(recording_frame)
            self.recordings.append(recording_frame)

        self.ui.recording_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.ui.recording_container_layout.addItem(self.ui.recording_verticalSpacer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
