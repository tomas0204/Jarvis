from pycaw.pycaw import AudioUtilities
from ctypes import POINTER, cast
import win32api
import win32con
from backend.commands.registry import CommandResult


class MediaCommands:

    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        self.volume = devices.EndpointVolume

    def volume_up(self):
        current = self.volume.GetMasterVolumeLevelScalar()
        new_volume = min(current + 0.05, 1.0)

        self.volume.SetMasterVolumeLevelScalar(
            new_volume,
            None
        )

        percentage = round(new_volume * 100)

        return CommandResult(
            True,
            f"Volumen al {percentage}%."
        )

    def volume_down(self):
        current = self.volume.GetMasterVolumeLevelScalar()
        new_volume = max(current - 0.05, 0.0)

        self.volume.SetMasterVolumeLevelScalar(
            new_volume,
            None
        )

        percentage = round(new_volume * 100)

        return CommandResult(
            True,
            f"Volumen al {percentage}%."
        )
    
    def set_volume(self, percentage):
        percentage = max(0, min(100, percentage))

        self.volume.SetMasterVolumeLevelScalar(
            percentage / 100,
            None
        )

        return CommandResult(
            True,
            f"Volumen al {percentage}%."
        )
        
    def mute(self):
        self.volume.SetMute(1, None)
        
        return CommandResult(
            True,
            "Se silenció el volumen."
        )
    
    def unmute(self):
        self.volume.SetMute(0, None)
        
        return CommandResult(
            True,
            "Volumen activado."
        )
    
    def pause(self):
        win32api.keybd_event(
            win32con.VK_MEDIA_PLAY_PAUSE,
            0,
            0,
            0
        )
        win32api.keybd_event(
            win32con.VK_MEDIA_PLAY_PAUSE,
            0,
            win32con.KEYEVENTF_KEYUP,
            0
        )

        return CommandResult(
            True,
            "Reproducción pausada."
        )