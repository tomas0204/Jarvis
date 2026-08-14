from ai.providers.groq import GroqProvider


class LLM:

    def __init__(self):
        self.provider = GroqProvider()
        self.messages = []

    def ask(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

        response = self.provider.ask(self.messages)

        self.messages.append({
            "role": "assistant",
            "content": response
        })

        return response