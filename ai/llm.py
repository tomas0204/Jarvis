from ai.providers.groq import GroqProvider


class LLM:

    def __init__(self):
        self.provider = GroqProvider()
    
    def ask(self, message):
        return self.provider.ask(message)