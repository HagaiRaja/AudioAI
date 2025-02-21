from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt


class SelectableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setTextInteractionFlags(
            Qt.TextSelectableByMouse)  # Enable text selection


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Use the custom SelectableLabel
        label = SelectableLabel("This is selectable and copyable text.")
        layout.addWidget(label)

        self.setLayout(layout)
        self.setWindowTitle("Selectable QLabel Example")


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
