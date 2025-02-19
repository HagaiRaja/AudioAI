# This Python file uses the following encoding: utf-8
import sys, os, time
import wave

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QFrame, QLabel, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtGui import (QFont, QCursor, QIcon)
from PySide6.QtCore import (Qt, QRect, QSize, QCoreApplication, QTimer)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Main
from audio_player import AudioPlayer
from audio_recorder import AudioRecorder

class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.refresh_recordings()
        self._init_audio()
        self._init_recorder()
        self._init_ui()

    def _init_ui(self):
        self.ui.menu_settings_button.clicked.connect(self.selectDirectoryDialog)
        self.ui.play_button.clicked.connect(self.toggle_play_pause)
        self.ui.audio_player_slider.sliderReleased.connect(self.seek_audio)
        self.ui.audio_player_slider.setMinimum(0)
        self.ui.forward_button.clicked.connect(lambda: self.shift_audio(10))
        self.ui.backward_button.clicked.connect(lambda: self.shift_audio(-10))
        self.ui.menu_record_button.clicked.connect(self.toggle_recording)

    def _init_audio(self):
        self.root_dir = "./sounds/"
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)
        self.recordings = []
        self.load_files()
        self.audio_player = AudioPlayer()
        self.audio_timer = QTimer()
        self.audio_timer.timeout.connect(self.update_audio_progress)
        self.is_audio_selected = False

    def _init_recorder(self):
        self.recorder = AudioRecorder()
        self.recorder.data_collected.connect(self.save_audio)
        self.recorder_timer = QTimer()
        self.recorder_timer.timeout.connect(self.update_recorder_progress)
        self.is_show_recorder = False

    def save_audio(self, audio_data):
        options = QFileDialog.Options()
        timestamp_str = self.recorder.timestamp.strftime("%Y-%m-%d_%H-%M-%S")
        default_filename = f"recording_{timestamp_str}.wav"
        default_path = os.path.join(self.root_dir, default_filename)
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Audio File", default_path, "WAV Files (*.wav)", options=options)
        if file_path:
            with wave.open(file_path, 'wb') as wf:
                wf.setnchannels(2)
                wf.setsampwidth(2)  # 16-bit audio
                wf.setframerate(44100)
                wf.writeframes(audio_data.tobytes())
            QMessageBox.information(self, "Success", f"Audio saved as {file_path}")
            self.load_files()
        self.ui.audio_player_duration.setText("00:00")

    def toggle_recording(self):
        if self.is_show_recorder:
            self.ui.forward_button.show()
            self.ui.backward_button.show()
            self.ui.play_button.setIcon(iconPlayRed)
            self.ui.menu_record_button.setIcon(iconRecordGray)
            self.ui.audio_player_slider.show()
            self.ui.audio_player_current_time.show()
            self.ui.audio_player_duration.setText("00:00")
            self.ui.audio_player_title.setText("Welcome to Audio AI")
            self.ui.audio_player_desc.setText("no file selected")
            self.is_audio_selected = False
            self.refresh_ui_player()
        else:
            if self.audio_player.is_playing:
                self.audio_player.stop()
                self.audio_timer.stop()
            self.ui.forward_button.hide()
            self.ui.backward_button.hide()
            self.ui.audio_player_slider.hide()
            self.ui.audio_player_slider.setValue(0)
            self.ui.audio_player_current_time.hide()
            self.ui.audio_player_duration.setText("00:00")
            self.ui.audio_player_title.setText("Record Audio")
            self.ui.audio_player_desc.setText("Click button to start/stop recording")
            self.ui.play_button.setIcon(iconRecordDotGray)
            self.ui.menu_record_button.setIcon(iconRecordRed)
        self.is_show_recorder = not self.is_show_recorder
    
    def shift_audio(self, seconds=10):
        if not self.is_audio_selected: return
        new_time = self.audio_player.current_time + seconds
        if new_time < 0:
            new_time = 0
        elif new_time > self.audio_player.duration_seconds:
            new_time = self.audio_player.duration_seconds
        prev_state = self.audio_player.is_playing
        self.audio_player.stop()
        self.audio_player.play(starts=new_time)
        self.ui.audio_player_current_time.setText(QCoreApplication.translate("Main", self.audio_player.get_current_time_str(), None))
        if prev_state:
            self.ui.play_button.setIcon(iconPauseRed)
            self.audio_timer.start(1000)
        else:
            self.ui.play_button.setIcon(iconPlayRed)
            self.audio_player.pause()
            self.ui.audio_player_slider.setValue(new_time)
            self.audio_timer.stop()

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

    def toggle_play_pause(self):
        if self.is_show_recorder:
            if self.recorder.isRunning():
                self.recorder.stop_recording()
                self.recorder_timer.stop()
                self.ui.play_button.setIcon(iconRecordDotGray)
            else:
                self.recorder.start()
                self.recorder_timer.start(1000)
                self.ui.play_button.setIcon(iconRecordDotRed)
        else:
            if not self.is_audio_selected: return
            if self.audio_player.is_playing:
                self.audio_player.pause()
                self.ui.play_button.setIcon(iconPlayRed)
                self.audio_timer.stop()
            else:
                if self.audio_player.current_time >= self.audio_player.duration_seconds:
                    # start from beginning
                    self.audio_player.play(starts=0)
                    self.ui.audio_player_slider.setValue(0)
                else:
                    self.audio_player.resume()
                self.ui.play_button.setIcon(iconPauseRed)
                self.audio_timer.start(1000)

    def update_audio_progress(self):
        if self.audio_player.is_playing:
            self.audio_player.current_time += 1  # Approximate time tracking
            if self.audio_player.current_time > self.audio_player.duration_seconds:
                self.audio_player.stop()
                self.audio_timer.stop()
                self.ui.play_button.setIcon(iconPlayRed)
                return
            self.ui.audio_player_slider.setValue(self.audio_player.current_time)
            self.ui.audio_player_current_time.setText(QCoreApplication.translate("Main", self.audio_player.get_current_time_str(), None))
        else:
            self.audio_timer.stop()

    def update_recorder_progress(self):
        # get the diff between current time and recorder timestamp
        diff = int((time.time() - self.recorder.timestamp.timestamp()))
        self.ui.audio_player_duration.setText(f"{diff//60:02}:{diff%60:02}")
    
    def seek_audio(self):
        new_time = self.ui.audio_player_slider.value()
        self.audio_player.stop()
        self.audio_player.play(starts=new_time)
        self.ui.audio_player_current_time.setText(QCoreApplication.translate("Main", self.audio_player.get_current_time_str(), None))
        self.ui.play_button.setIcon(iconPauseRed)
        self.audio_timer.start(1000)

    def refresh_ui_player(self):
        if self.is_audio_selected:
            self.ui.audio_player_duration.setText(
                QCoreApplication.translate("Main",self.audio_player.duration_str, None))
            self.ui.audio_player_current_time.setText(
                QCoreApplication.translate("Main", self.audio_player.get_current_time_str(), None))
            if self.audio_player.is_playing:
                self.ui.play_button.setIcon(iconPauseRed)
            else:
                self.ui.play_button.setIcon(iconPlayRed)
            self.ui.forward_button.setIcon(iconForwardRed)
            self.ui.backward_button.setIcon(iconBackwardRed)
        else:
            self.ui.audio_player_duration.setText("00:00")
            self.ui.audio_player_current_time.setText("00:00")
            self.ui.play_button.setIcon(iconPlayGray)
            self.ui.forward_button.setIcon(iconForwardGray)
            self.ui.backward_button.setIcon(iconBackwardGray)
        self.ui.audio_player_slider.setValue(0)

    def setup_player(self, filepath, created_at):
        if self.is_show_recorder:
            self.toggle_recording()
        print(f"Playing: {filepath} created at {created_at}")
        self.ui.audio_player_title.setText(QCoreApplication.translate("Main", filepath, None))
        self.ui.audio_player_desc.setText(QCoreApplication.translate("Main", created_at, None))
        self.audio_player.open(os.path.join(self.root_dir, filepath))
        self.ui.audio_player_slider.setMaximum(self.audio_player.duration_seconds)
        self.audio_player.current_time = 0
        self.audio_timer.stop()
        self.audio_player.play()
        self.ui.play_button.setIcon(iconPauseRed)
        self.audio_timer.start(1000)
        self.is_audio_selected = True
        self.refresh_ui_player()

    def load_files(self):
        files = [] # contains pair of (relative path to root_dir, created_at)
        for root, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                # only include audio files
                if not filename.endswith((".wav", ".mp3", ".ogg", ".m4a")): continue
                if "converted" in filename: continue
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
            recording_frame.setStyleSheet(u"QFrame:hover {background-color:#FFC9C9}")
            recording_frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            recording_frame.setFrameShape(QFrame.StyledPanel)
            recording_frame.setFrameShadow(QFrame.Raised)
            verticalLayout = QVBoxLayout(recording_frame)
            verticalLayout.setSpacing(0)
            verticalLayout.setObjectName(f"verticalLayout_{id}")
            verticalLayout.setContentsMargins(5, 0, 0, 0)
            # if recording_frame is clicked, setup the player
            recording_frame.mousePressEvent = lambda event, fp=filepath, ca=created_at: self.setup_player(fp, ca)

            recording_title = QLabel(recording_frame)
            recording_title.setObjectName(f"recording{id}_title")
            font2 = QFont()
            font2.setFamilies([u"Poppins"])
            font2.setBold(True)
            recording_title.setFont(font2)
            recording_title.setStyleSheet(u"QLabel {color: #333;"
                                          "background-color:transparent;}")
            verticalLayout.addWidget(recording_title)
            recording_title.setText(QCoreApplication.translate("Main", filepath, None))

            recording_datetime = QLabel(recording_frame)
            recording_datetime.setObjectName(f"recording{id}_datetime")
            font3 = QFont()
            font3.setFamilies([u"Poppins"])
            font3.setItalic(False)
            recording_datetime.setFont(font3)
            recording_datetime.setStyleSheet(u"QLabel {color: #858585;"
                                          "background-color:transparent;}")
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
    from icons import (
        iconPlayRed, iconPlayGray, iconPauseRed,
        iconRecordGray, iconRecordRed,
        iconRecordDotGray, iconRecordDotRed,
        iconForwardGray, iconForwardRed,
        iconBackwardGray, iconBackwardRed
    )
    widget.show()
    sys.exit(app.exec())
