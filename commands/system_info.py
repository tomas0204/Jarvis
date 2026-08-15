from datetime import datetime
from commands.registry import CommandResult

class SystemInfoCommands:
    def get_time(self):
        current_time = datetime.now().strftime("%H:%M")

        return CommandResult(
            True,
            f"Son las {current_time}."
        )
        
    def get_date(self):
        current_date = datetime.now().strftime("%d/%m/%Y")

        return CommandResult(
            True,
            f"Hoy es {current_date}."
        )