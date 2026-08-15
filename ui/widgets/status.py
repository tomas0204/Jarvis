from PySide6.QtWidgets import QLabel


class StatusWidget(QLabel):

    def __init__(self):
        super().__init__("● IDLE")

        self.setObjectName("status")