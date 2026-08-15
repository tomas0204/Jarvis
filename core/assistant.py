from voice.speech_to_text   import SpeechToText
from voice.text_to_speech   import TextToSpeech
from ai.llm                 import LLM
from core.intent            import Intent
from commands.system        import SystemCommands
from config                 import APPLICATIONS

class Assistant:
    def __init__(self):
        self.stt = SpeechToText()
        self.commands = SystemCommands()
        self.tts = TextToSpeech()
        self.llm = LLM()
        self.intent = Intent()
        
    def listen(self):
        audio = self.stt.listen()

        if audio is None:
            return None

        return self.stt.transcribe(audio)

    def run_once(self):
        text = self.listen()

        if not text:
            return True

        intent = self.intent.detect(text)

        if intent == "exit":
            self.tts.speak("Hasta luego. ¡Que tengas un buen día!")
            return False
        if intent == "open_chrome":
            success = self.commands.open_application(APPLICATIONS["chrome"])

            if success:
                self.tts.speak("Abriendo Chrome.")
            else:
                self.tts.speak("No pude abrir Chrome.")

                return True
        self.process(text)

        return True
        
    def process(self, text):
        response = self.llm.ask(text)
        self.tts.speak(response)
        return response
    
    def run(self):
        self.stt.calibrate()

        while self.run_once():
            pass