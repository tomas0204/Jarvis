from PySide6.QtWidgets import QPushButton


class MicrophoneWidget(QPushButton):

    def __init__(self):
        super().__init__("🎙 Escuchar")

        self.setObjectName("microphone")