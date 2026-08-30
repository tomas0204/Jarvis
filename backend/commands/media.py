from pycaw.pycaw import AudioUtilities

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