import os

class SystemCommands:
    
    def open_application(self, application):
        try:
            os.startfile(application)
            return True
        except OSError:
            return False