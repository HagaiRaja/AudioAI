import sys
import sounddevice as sd
import numpy as np
import wave
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal

class AudioRecorder(QThread):
    data_collected = Signal(np.ndarray)

    def __init__(self, sample_rate=44100, channels=2):
        super().__init__()
        self.sample_rate = sample_rate
        self.channels = channels
        self.is_recording = False
        self.audio_data = []

    def run(self):
        self.is_recording = True
        self.audio_data = []
        with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, dtype=np.int16, callback=self.callback):
            while self.is_recording:
                sd.sleep(100)

    def callback(self, indata, frames, time, status):
        if status:
            print(f"Recording Error: {status}")
        self.audio_data.append(indata.copy())

    def stop_recording(self):
        self.is_recording = False
        self.wait()  # Wait for thread to finish
        if self.audio_data:
            self.data_collected.emit(np.concatenate(self.audio_data, axis=0))  # Send data to main thread

class AudioRecorderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.recorder = AudioRecorder()
        self.recorder.data_collected.connect(self.save_audio)

    def init_ui(self):
        self.setWindowTitle("Audio Recorder")
        self.setGeometry(100, 100, 300, 150)
        layout = QVBoxLayout()

        self.record_button = QPushButton("Start Recording")
        self.record_button.clicked.connect(self.toggle_recording)
        layout.addWidget(self.record_button)

        self.setLayout(layout)

    def toggle_recording(self):
        if self.recorder.isRunning():
            self.recorder.stop_recording()
            self.record_button.setText("Start Recording")
        else:
            self.recorder.start()
            self.record_button.setText("Stop Recording")

    def save_audio(self, audio_data):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Audio File", "", "WAV Files (*.wav)", options=options)
        if file_path:
            with wave.open(file_path, 'wb') as wf:
                wf.setnchannels(2)
                wf.setsampwidth(2)  # 16-bit audio
                wf.setframerate(44100)
                wf.writeframes(audio_data.tobytes())
            QMessageBox.information(self, "Success", f"Audio saved as {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioRecorderApp()
    window.show()
    sys.exit(app.exec())
