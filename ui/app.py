import sys

from PySide6.QtWidgets import QApplication

from ui.window import MainWindow


def run():
    app = QApplication(sys.argv)

    with open("ui/styles/main.qss", "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())