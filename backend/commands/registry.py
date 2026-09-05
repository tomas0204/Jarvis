class CommandResult:

    def __init__(self, success, response):
        self.success = success
        self.response = response

class CommandRegistry:

    def __init__(self):
        self.commands = {}

    def register(self, name, function):
        self.commands[name] = function

    def execute(self, name, args=None):
        command = self.commands.get(name)

        if not command:
            return CommandResult(
                False,
                f"Comando desconocido: {name}"
            )

        args = args or {}

        try:
            return command(**args)

        except Exception as e:
            return CommandResult(
                False,
                f"Error ejecutando el comando: {e}"
            )