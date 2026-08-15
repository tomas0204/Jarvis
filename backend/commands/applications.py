from backend.commands.registry  import CommandResult
from config             import APPLICATIONS
    

class ApplicationCommands:

    def __init__(self, system):
        self.system = system

    def open(self, application):
        path = APPLICATIONS.get(application)

        if path is None:
            return CommandResult(
                False,
                "No conozco esa aplicación."
            )

        success = self.system.open_application(path)

        if success:
            return CommandResult(
                True,
                f"Abriendo {application}."
            )
