from  backend.commands.applications import ApplicationCommands
from  backend.commands.system_info  import SystemInfoCommands
from  backend.commands.web          import WebCommands
from  backend.commands.media        import MediaCommands

def register_commands(registry, system):
    applications = ApplicationCommands(system)
    system_info = SystemInfoCommands()
    media = MediaCommands()
    
    registry.register(
        "open_application",
        applications.open
    )

    registry.register(
        "get_time",
        system_info.get_time
    )
    
    registry.register(
        "get_date",
        system_info.get_date
    )
    
    web = WebCommands()

    registry.register(
        "open_website",
        web.open_website
    )
    
    registry.register(
        "search_website",
        web.search_website
    )
    
    registry.register(
        "volume_up",
        media.volume_up
    )
    
    registry.register(
        "volume_down",
        media.volume_down
    )
    
    registry.register(
        "set_volume",
        media.set_volume
    )

    registry.register(
        "mute",
        media.mute
    )
    
    registry.register(
        "unmute",
        media.unmute
    )
    
    registry.register(
        "pause",
        media.pause
    )
    

    
