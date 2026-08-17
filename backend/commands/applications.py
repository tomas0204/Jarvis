from backend.commands.registry import CommandResult
from config import APPLICATIONS


class ApplicationCommands:

    def __init__(self, system):
        self.system = system

    def open(self, name):
        path = APPLICATIONS.get(name)

        if path is None:
            return CommandResult(
                False,
                "No conozco esa aplicación."
            )

        success = self.system.open_application(path)

        if success:
            return CommandResult(
                True,
                f"Abriendo {name}."
            )

        return CommandResult(
            False,
            f"No pude abrir {name}."
        )