from commands.applications import ApplicationCommands
from commands.system_info import SystemInfoCommands


def register_commands(registry, system):
    applications = ApplicationCommands(system)
    system_info = SystemInfoCommands()

    registry.register(
        "open_chrome",
        lambda: applications.open("chrome")
    )

    registry.register(
        "open_steam",
        lambda: applications.open("steam")
    )

    registry.register(
        "get_time",
        system_info.get_time
    )
    
    registry.register(
        "get_date",
        system_info.get_date
    )