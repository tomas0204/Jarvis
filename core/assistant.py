from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech
from ai.llm import LLM

class Assistant:
    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.llm = LLM()
        
    def listen(self):
        audio = self.stt.listen()

        if audio is None:
            return None

        return self.stt.transcribe(audio)

    def run_once(self):
        text = self.listen()

        if not text:
            return

        self.process(text)
        
    def process(self, text):
        response = self.llm.ask(text)
        self.tts.speak(response)

        return response