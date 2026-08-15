from config import APPLICATIONS


class ApplicationCommands:

    def __init__(self, system):
        self.system = system

    def open_chrome(self):
        return self.system.open_application(
            APPLICATIONS["chrome"]
        )
    def open_steam(self):
        return self.system.open_application(
            APPLICATIONS["steam"]
        )