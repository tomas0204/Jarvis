class CommandResult:

    def __init__(self, success, response):
        self.success = success
        self.response = response

class CommandRegistry:

    def __init__(self):
        self.commands = {}

    def register(self, name, function):
        self.commands[name] = function

    def execute(self, name):
        command = self.commands.get(name)
        print(f"Executing command: {name}")  # Debugging line
        if command is None:
            return CommandResult(
                False,
                "No conozco ese comando."
            )

        return command()