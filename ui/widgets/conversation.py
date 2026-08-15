from PySide6.QtWidgets import QTextEdit


class ConversationWidget(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.setObjectName("conversation")

    def add_user_message(self, message):
        self.append(f"Tú: {message}")

    def add_jarvis_message(self, message):
        self.append(f"JARVIS: {message}")