# This Python file uses the following encoding: utf-8
import sys
import os
import time
import shutil
import wave
import json

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QFrame, QLabel, QSpacerItem, QSizePolicy, QMessageBox
from PySide6.QtGui import (QFont, QCursor, QIcon)
from PySide6.QtCore import (Qt, QRect, QSize, QCoreApplication, QTimer)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Main
from helper.audio_player import AudioPlayer
from helper.audio_recorder import AudioRecorder
from helper.transcribe import Transcribe
from helper.ollama_helper import generate_response_stream
from custom_widget.selectable_label import SelectableLabel


class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self._init_ui()
        self.refresh_recordings()
        self.refresh_chat()
        self._init_audio()
        self._init_recorder()
        self._init_chat()
        self._init_ai()

    def _init_ui(self):
        self.ui.menu_settings_button.clicked.connect(
            self.select_directory_dialog)
        self.ui.play_button.clicked.connect(self.toggle_play_pause)
        self.ui.audio_player_slider.sliderReleased.connect(self.seek_audio)
        self.ui.audio_player_slider.setMinimum(0)
        self.ui.forward_button.clicked.connect(lambda: self.shift_audio(10))
        self.ui.backward_button.clicked.connect(lambda: self.shift_audio(-10))
        self.ui.menu_record_button.clicked.connect(self.toggle_recording)
        self.ui.menu_import_button.clicked.connect(self.import_file)
        self.ui.ai_chatbox_input_button.clicked.connect(self.send_message)

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

    def _init_chat(self):
        self.chat_history = []
        # when ai_chatbox_input_textarea is pressed with Ctrl/Cmd + Enter, send message and for other just do as usual
        original_keyPressEvent = self.ui.ai_chatbox_input_textarea.keyPressEvent
        self.ui.ai_chatbox_input_textarea.keyPressEvent = \
            lambda event: self.send_message() \
            if (event.modifiers() & Qt.ControlModifier) \
            and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter) \
            else original_keyPressEvent(event)

        self.ui.clear_chat_button.clicked.connect(self.clear_chat)
        self.ui.ai_chatbox_input_textarea.setReadOnly(True)

    def get_file_for(self, purpose):
        extension = "." + self.audio_player.filepath.split(".")[-1]
        if purpose == "chat":
            return self.audio_player.filepath.replace(extension, "_chat.json")
        elif purpose == "transcription":
            return self.audio_player.filepath.replace(extension, "_transcription.json")

    def clear_chat(self):
        self.chat_history = []
        self.refresh_chat()
        chat_file = self.get_file_for("chat")
        if os.path.exists(chat_file):
            os.remove(chat_file)

    def _init_ai(self):
        self.transcriber = Transcribe()
        self.ui.transcribe_container.mousePressEvent = lambda event: self.transcribe_audio()
        self.ui.alignment_container.mousePressEvent = lambda event: self.align_transcription()
        self.ui.diarization_container.mousePressEvent = lambda event: self.diarize_transcription()
        self.ui.transcription_content = QWidget()
        self.ui.transcription_scrollArea.setWidget(
            self.ui.transcription_content)

    def store_transcription(self):
        transcription_file = self.get_file_for("transcription")
        with open(transcription_file, "w") as f:
            json.dump(self.transcription, f)

    def transcribe_audio(self):
        if not self.is_audio_selected:
            return
        if self.transcription_status != "None":  # already transcribed
            return

        self.ui.transcribe_container.setStyleSheet(u"background-color: #F00;\n"
                                                   "border-radius: 10px;")
        QCoreApplication.processEvents()
        self.transcription = self.transcriber.transcribe_audio(
            self.audio_player.filepath)
        self.store_transcription()
        self.transcription_status = "Transcribed"
        self.ui.transcribe_container.setStyleSheet(u"background-color: #2B2B2B;\n"
                                                   "border-radius: 10px;")
        QCoreApplication.processEvents()
        self.refresh_transcription_status()

    def align_transcription(self):
        if not self.is_audio_selected:
            return
        if self.transcription_status == "None":
            self.transcribe_audio()
        if self.transcription_status != "Transcribed":  # already aligned
            return

        self.ui.alignment_container.setStyleSheet(u"background-color: #F00;\n"
                                                  "border-radius: 10px;")
        QCoreApplication.processEvents()
        self.transcription = self.transcriber.align_transcription(
            self.transcription, self.audio_player.filepath)
        self.store_transcription()
        self.transcription_status = "Aligned"
        self.ui.alignment_container.setStyleSheet(u"background-color: #2B2B2B;\n"
                                                  "border-radius: 10px;")
        QCoreApplication.processEvents()
        self.refresh_transcription_status()

    def diarize_transcription(self):
        if not self.is_audio_selected:
            return
        if self.transcription_status == "None":
            self.transcribe_audio()
        if self.transcription_status == "Transcribed":
            self.align_transcription()
        if self.transcription_status != "Aligned":  # already diarized
            return

        self.ui.diarization_container.setStyleSheet(u"background-color: #F00;\n"
                                                    "border-radius: 10px;")
        QCoreApplication.processEvents()
        self.transcription = self.transcriber.diarize_transcription(
            self.transcription, self.audio_player.filepath)
        self.store_transcription()
        self.transcription_status = "Diarized"
        self.ui.diarization_container.setStyleSheet(u"background-color: #2B2B2B;\n"
                                                    "border-radius: 10px;")
        QCoreApplication.processEvents()
        self.refresh_transcription_status()

    def save_audio(self, audio_data):
        options = QFileDialog.Options()
        timestamp_str = self.recorder.timestamp.strftime("%Y-%m-%d_%H-%M-%S")
        default_filename = f"recording_{timestamp_str}.wav"
        default_path = os.path.join(self.root_dir, default_filename)
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Audio File", default_path, "WAV Files (*.wav)", options=options)
        if file_path:
            with wave.open(file_path, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)  # 16-bit audio
                wf.setframerate(44100)
                wf.writeframes(audio_data.tobytes())
            QMessageBox.information(
                self, "Success", f"Audio saved as {file_path}")
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
            self.transcription_status = ""
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
            self.ui.audio_player_desc.setText(
                "Click button to start/stop recording")
            self.ui.play_button.setIcon(iconRecordDotGray)
            self.ui.menu_record_button.setIcon(iconRecordRed)
        self.is_show_recorder = not self.is_show_recorder
        self.render_transcription()
        self.refresh_chat()
        self.ui.ai_chatbox_input_textarea.setReadOnly(True)
        self.ui.ai_chatbox_input_textarea.clear()

    def shift_audio(self, seconds=10):
        if not self.is_audio_selected:
            return
        new_time = self.audio_player.current_time + seconds
        if new_time < 0:
            new_time = 0
        elif new_time > self.audio_player.duration_seconds:
            new_time = self.audio_player.duration_seconds
        prev_state = self.audio_player.is_playing
        self.audio_player.stop()
        self.audio_player.play(starts=new_time)
        self.ui.audio_player_current_time.setText(QCoreApplication.translate(
            "Main", self.audio_player.get_current_time_str(), None))
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
        self.ui.recording_container_content.setObjectName(
            u"recording_container_content")
        self.ui.recording_container_content.setGeometry(QRect(0, 0, 174, 397))
        self.ui.recording_container_layout = QVBoxLayout(
            self.ui.recording_container_content)
        self.ui.recording_container_layout.setObjectName(
            u"recording_container_layout")
        self.ui.recording_container_scrollArea.setWidget(
            self.ui.recording_container_content)

    def refresh_chat(self):
        self.ui.ai_chatbox_history_content = QWidget()
        self.ui.ai_chatbox_history_content.setObjectName(
            u"ai_chatbox_history_content")
        self.ui.ai_chatbox_history_content.setGeometry(QRect(0, 0, 174, 397))
        self.ui.ai_chatbox_history_layout = QVBoxLayout(
            self.ui.ai_chatbox_history_content)
        self.ui.ai_chatbox_history_layout.setObjectName(
            u"ai_chatbox_history_layout")
        self.ui.ai_chatbox_history_layout.setContentsMargins(0, 12, 0, 0)
        self.ui.ai_chatbox_history_layout.setSpacing(5)
        self.ui.ai_chatbox_history_scrollArea.setWidget(
            self.ui.ai_chatbox_history_content)
        self.ui.ai_chatbox_verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.ui.ai_chatbox_history_layout.addItem(
            self.ui.ai_chatbox_verticalSpacer)
        self.chat_history = []

    def store_chat(self):
        chat_file = self.get_file_for("chat")
        with open(chat_file, "w") as f:
            json.dump(self.chat_history, f)

    def generate_qt_chat(self, message, sender):
        if sender == "bot":
            color = "#868686"
        else:
            color = "#575757"
        qt_label = QFrame()
        qt_label.setObjectName(f"ai_chatbox_{sender}_{len(self.chat_history)}")
        qt_label.setStyleSheet(
            f"background-color: {color};\nborder-radius: 10px;")
        qt_label.setFrameShape(QFrame.StyledPanel)
        qt_label.setFrameShadow(QFrame.Raised)
        qt_label_layout = QVBoxLayout(qt_label)
        qt_label_layout.setObjectName(
            f"ai_chatbox_{sender}_verticalLayout_{len(self.chat_history)}")
        qt_label_content = SelectableLabel(message, qt_label)
        qt_label_content.setObjectName(
            f"ai_chatbox_{sender}{len(self.chat_history)}_label")
        qt_label_content.setStyleSheet(u"color: #FFF;")
        if sender == "human":
            qt_label_content.setAlignment(
                Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        qt_label_content.setWordWrap(True)
        qt_label_layout.addWidget(qt_label_content)
        return qt_label

    def refresh_chat_textarea(self):
        # Clear the input area
        self.ui.ai_chatbox_input_textarea.clear()
        if self.is_audio_selected:
            self.ui.ai_chatbox_input_textarea.setReadOnly(False)

        # Scroll to the bottom of the chat history
        QTimer.singleShot(100, lambda: self.ui.ai_chatbox_history_scrollArea.verticalScrollBar().setValue(
            self.ui.ai_chatbox_history_scrollArea.verticalScrollBar().maximum()
        ))

    def send_message(self):
        prompt = self.ui.ai_chatbox_input_textarea.toPlainText().strip()
        self.refresh_chat_textarea()
        if not prompt:
            return  # Do nothing if the message is empty

        human_label = self.generate_qt_chat(prompt, "human")
        self.ui.ai_chatbox_history_layout.addWidget(human_label)
        self.chat_history.append(("human", prompt))

        response = ""
        bot_label = self.generate_qt_chat(response, "bot")
        self.ui.ai_chatbox_history_layout.addWidget(bot_label)

        for chunk in generate_response_stream(prompt):
            response += chunk
            bot_label.findChild(SelectableLabel).setText(response)
            QCoreApplication.processEvents()
            QTimer.singleShot(100, lambda: self.ui.ai_chatbox_history_scrollArea.verticalScrollBar().setValue(
                self.ui.ai_chatbox_history_scrollArea.verticalScrollBar().maximum()))
            QCoreApplication.processEvents()
        self.chat_history.append(("bot", response))

        self.store_chat()

    def select_directory_dialog(self):
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
            if not self.is_audio_selected:
                return
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
            self.ui.audio_player_slider.setValue(
                self.audio_player.current_time)
            self.ui.audio_player_current_time.setText(QCoreApplication.translate(
                "Main", self.audio_player.get_current_time_str(), None))
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
        self.ui.audio_player_current_time.setText(QCoreApplication.translate(
            "Main", self.audio_player.get_current_time_str(), None))
        self.ui.play_button.setIcon(iconPauseRed)
        self.audio_timer.start(1000)

    def refresh_ui_player(self):
        if self.is_audio_selected:
            self.ui.audio_player_duration.setText(
                QCoreApplication.translate("Main", self.audio_player.duration_str, None))
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
        self.ui.audio_player_title.setText(
            QCoreApplication.translate("Main", filepath, None))
        self.ui.audio_player_desc.setText(
            QCoreApplication.translate("Main", created_at, None))
        self.audio_player.open(os.path.join(self.root_dir, filepath))
        self.ui.audio_player_slider.setMaximum(
            self.audio_player.duration_seconds)
        self.audio_player.current_time = 0
        self.audio_timer.stop()
        self.audio_player.play()
        self.audio_player.pause()
        self.ui.play_button.setIcon(iconPlayRed)
        self.is_audio_selected = True
        self.refresh_ui_player()

    def check_transcription_status(self, transcription):
        if "word_segments" in transcription:
            for segment in transcription["word_segments"]:
                if "speaker" in segment:
                    return "Diarized"
            return "Aligned"
        return "Transcribed"

    def load_transcription(self, filepath):
        extension = "." + filepath.split(".")[-1]
        transcription_file = os.path.join(
            self.root_dir, filepath.replace(extension, "_transcription.json"))
        print(transcription_file)
        if not os.path.exists(transcription_file):
            return "None", None
        transcription = json.load(open(transcription_file, "r"))
        status = self.check_transcription_status(transcription)
        return status, transcription

    def audio_jump_to(self, timestamp):
        self.audio_player.stop()
        self.audio_player.play(starts=timestamp)
        self.ui.audio_player_slider.setValue(timestamp)
        self.ui.audio_player_current_time.setText(QCoreApplication.translate(
            "Main", self.audio_player.get_current_time_str(), None))
        self.ui.play_button.setIcon(iconPauseRed)
        self.audio_timer.start(1000)

    def render_transcription(self):
        self.ui.transcription_content = QWidget()
        self.ui.transcription_content.setObjectName(
            u"transcription_content")
        self.ui.transcription_content.setGeometry(QRect(0, 0, 174, 397))
        self.ui.transcription_layout = QVBoxLayout(
            self.ui.transcription_content)
        self.ui.transcription_layout.setObjectName(
            u"transcription_layout")
        self.ui.transcription_layout.setContentsMargins(5, 5, 0, 0)
        self.ui.transcription_layout.setSpacing(5)
        self.ui.transcription_scrollArea.setWidget(
            self.ui.transcription_content)

        def int2hour(seconds):
            hh, mm, ss = seconds // 3600, (seconds % 3600) // 60, seconds % 60
            if hh == 0:
                return f"{mm:02}:{ss:02}"
            return f"{hh:02}:{mm:02}:{ss:02}"

        def generate_qt_segment(text, timestamp, color, speakerId, segmentId):
            qt_segment = QFrame()
            qt_segment.setObjectName(
                f"transcription_speaker_{speakerId}_{segmentId}")
            qt_segment.setStyleSheet(f"background-color: {color};\n"
                                     "border-radius: 10px;")
            qt_segment.setFrameShape(QFrame.StyledPanel)
            qt_segment.setFrameShadow(QFrame.Raised)
            qt_segment_layout = QVBoxLayout(qt_segment)
            qt_segment_layout.setSpacing(0)
            qt_segment_layout.setObjectName(
                f"verticalLayout_{speakerId}_{segmentId}")
            qt_segment_layout.setContentsMargins(10, 5, 5, 5)

            qt_segment_time = QLabel(qt_segment)
            qt_segment_time.setObjectName(
                f"transcription_speaker_{speakerId}_{segmentId}_time")
            qt_segment_time.setCursor(
                QCursor(Qt.CursorShape.PointingHandCursor))
            qt_segment_time.setStyleSheet(u"color: #FFF;")
            qt_segment_time.setAlignment(
                Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            qt_segment_time.setText(
                QCoreApplication.translate("Main", f"{int2hour(timestamp)}", None))
            qt_segment_time.mousePressEvent = lambda event, st=timestamp: self.audio_jump_to(
                st)
            qt_segment_layout.addWidget(qt_segment_time)

            qt_segment_label = SelectableLabel(text, qt_segment)
            qt_segment_label.setObjectName(
                f"transcription_speaker_{speakerId}_{segmentId}_label")
            qt_segment_label.setFont(font5)
            qt_segment_label.setStyleSheet(u"color: #FFF;")
            qt_segment_label.setWordWrap(True)
            qt_segment_layout.addWidget(qt_segment_label)

            return qt_segment

        if not self.is_show_recorder:
            if self.transcription_status == "None":
                self.ui.transcription_layout.addWidget(generate_qt_segment(
                    "No transcription available.\n\n"
                    "Click the Transcribe/Alignment/Diarization button to start!", 0, "#575757", 0, 0))
            elif self.transcription_status in ["Transcribed", "Aligned"]:
                for idx, segment in enumerate(self.transcription["segments"]):
                    self.ui.transcription_layout.addWidget(generate_qt_segment(
                        segment["text"], int(segment['start']), "#575757", 0, idx))
            elif self.transcription_status == "Diarized":
                for idx, segment in enumerate(self.transcription["segments"]):
                    speaker_id, color = "99", "#000"
                    if "speaker" in segment:
                        speaker_id = int(segment["speaker"].split("_")[-1])
                        color = colors[speaker_id % len(colors)]
                    self.ui.transcription_layout.addWidget(generate_qt_segment(
                        segment["text"], int(segment['start']), color, speaker_id, idx))

        self.ui.transcription_verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.ui.transcription_layout.addItem(
            self.ui.transcription_verticalSpacer)

    def refresh_transcription_status(self):
        if self.transcription_status == "None":
            self.ui.transcribe_icon.setIcon(iconSoundGray)
            self.ui.alignment_icon.setIcon(iconSoundGray)
            self.ui.diarization_icon.setIcon(iconSoundGray)
        elif self.transcription_status == "Transcribed":
            self.ui.transcribe_icon.setIcon(iconSoundRed)
            self.ui.alignment_icon.setIcon(iconSoundGray)
            self.ui.diarization_icon.setIcon(iconSoundGray)
        elif self.transcription_status == "Aligned":
            self.ui.transcribe_icon.setIcon(iconSoundRed)
            self.ui.alignment_icon.setIcon(iconSoundRed)
            self.ui.diarization_icon.setIcon(iconSoundGray)
        elif self.transcription_status == "Diarized":
            self.ui.transcribe_icon.setIcon(iconSoundRed)
            self.ui.alignment_icon.setIcon(iconSoundRed)
            self.ui.diarization_icon.setIcon(iconSoundRed)

        self.render_transcription()

    def setup_chat(self):
        print("Setting up chat")
        self.refresh_chat()
        self.chat_history = []
        chat_file = self.get_file_for("chat")
        if os.path.exists(chat_file):
            self.chat_history = json.load(open(chat_file, "r"))
            for sender, message in self.chat_history:
                qt_label = self.generate_qt_chat(message, sender)
                self.ui.ai_chatbox_history_layout.addWidget(qt_label)

        self.refresh_chat_textarea()

    def setup_workstation(self, filepath, created_at):
        self.setup_player(filepath, created_at)
        # check latest status of transcription
        self.transcription_status, self.transcription = self.load_transcription(
            filepath)
        self.refresh_transcription_status()
        self.setup_chat()

    def load_files(self):
        files = []  # contains pair of (relative path to root_dir, created_at)
        for root, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                # only include audio files
                if not filename.endswith((".wav", ".mp3", ".ogg", ".m4a")):
                    continue
                if "converted" in filename:
                    continue
                filepath = os.path.relpath(
                    os.path.join(root, filename), self.root_dir)
                created_at = os.path.getctime(os.path.join(root, filename))
                # convert created_at to human readable format e.g. Mon, 2021-09-01 12:00
                created_at = time.strftime(
                    "%a, %Y-%m-%d %H:%M", time.localtime(created_at))
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
            recording_frame.setStyleSheet(
                u"QFrame:hover {background-color:#FFC9C9}")
            recording_frame.setCursor(
                QCursor(Qt.CursorShape.PointingHandCursor))
            recording_frame.setFrameShape(QFrame.StyledPanel)
            recording_frame.setFrameShadow(QFrame.Raised)
            verticalLayout = QVBoxLayout(recording_frame)
            verticalLayout.setSpacing(0)
            verticalLayout.setObjectName(f"verticalLayout_{id}")
            verticalLayout.setContentsMargins(5, 0, 0, 0)
            # if recording_frame is clicked, setup the player
            recording_frame.mousePressEvent = lambda event, fp=filepath, ca=created_at: self.setup_workstation(
                fp, ca)

            recording_title = QLabel(recording_frame)
            recording_title.setObjectName(f"recording{id}_title")
            font2 = QFont()
            font2.setFamilies([u"Poppins"])
            font2.setBold(True)
            recording_title.setFont(font2)
            recording_title.setStyleSheet(u"QLabel {color: #333;"
                                          "background-color:transparent;}")
            recording_title.setText(QCoreApplication.translate(
                "Main", filepath, None))
            verticalLayout.addWidget(recording_title)

            recording_datetime = QLabel(recording_frame)
            recording_datetime.setObjectName(f"recording{id}_datetime")
            font3 = QFont()
            font3.setFamilies([u"Poppins"])
            font3.setItalic(False)
            recording_datetime.setFont(font3)
            recording_datetime.setStyleSheet(u"QLabel {color: #858585;"
                                             "background-color:transparent;}")
            recording_datetime.setText(QCoreApplication.translate(
                "Main", created_at, None))
            verticalLayout.addWidget(recording_datetime)

            # Add to layout and storage
            self.ui.recording_container_layout.addWidget(recording_frame)
            self.recordings.append(recording_frame)

        self.ui.recording_verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.ui.recording_container_layout.addItem(
            self.ui.recording_verticalSpacer)

    def import_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Audio File", "", "Audio Files (*.wav *.mp3 *.ogg *.m4a)", options=options)
        if file_path:
            filename = os.path.basename(file_path)
            new_path = os.path.join(self.root_dir, filename)
            if new_path != file_path:
                shutil.copy(file_path, new_path)
            self.load_files()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    from helper.constant import (
        iconPlayRed, iconPlayGray, iconPauseRed,
        iconRecordGray, iconRecordRed,
        iconRecordDotGray, iconRecordDotRed,
        iconForwardGray, iconForwardRed,
        iconBackwardGray, iconBackwardRed,
        iconSoundGray, iconSoundRed,
        font5, colors
    )
    widget.show()
    sys.exit(app.exec())
