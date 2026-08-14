from ai.providers.groq import GroqProvider
from config import LLM_MAX_HISTORY

class LLM:

    def __init__(self):
        self.provider = GroqProvider()
        self.messages = []

    def ask(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })
        self.messages = self.messages[-LLM_MAX_HISTORY:]
        response = self.provider.ask(self.messages)

        self.messages.append({
            "role": "assistant",
            "content": response
        })
        
        self.messages = self.messages[-LLM_MAX_HISTORY:]

        return response