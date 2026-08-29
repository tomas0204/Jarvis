import os
import subprocess

class SystemCommands:

    def open_application(self, application_type, value):
        try:
            if application_type == "path":
                os.startfile(value)

            elif application_type == "uri":
                subprocess.Popen(
                    ["cmd", "/c", "start", "", value],
                    shell=False
                )

            else:
                return False

            return True

        except OSError:
            return False