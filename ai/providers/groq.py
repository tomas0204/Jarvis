from groq       import Groq
from config     import GROQ_API_KEY, LLM_MODEL, LLM_SYSTEM_PROMPT

class GroqProvider:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
    
    def ask(self, message):
        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": LLM_SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message.content