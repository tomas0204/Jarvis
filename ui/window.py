from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout
)

from ui.widgets.status import StatusWidget
from ui.widgets.conversation import ConversationWidget
from ui.widgets.microphone import MicrophoneWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S")
        self.resize(900, 600)

        self._setup_ui()

    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.status = StatusWidget()
        self.conversation = ConversationWidget()
        self.microphone = MicrophoneWidget()

        self.conversation.add_user_message("abre YouTube")
        self.conversation.add_jarvis_message("Abriendo YouTube.")

        layout.addWidget(self.status)
        layout.addWidget(self.conversation)
        layout.addWidget(self.microphone)