from backend.commands.setup         import register_commands
from backend.voice.speech_to_text   import SpeechToText
from backend.voice.text_to_speech   import TextToSpeech
from backend.ai.llm                 import LLM
from backend.core.intent            import Intent
from backend.commands.system        import SystemCommands
from backend.commands.registry      import CommandRegistry

class Assistant:
    def __init__(self):
        self.stt = SpeechToText()
        self.commands = SystemCommands()
        self.registry = CommandRegistry()
        self.system = SystemCommands()
        self.registry = CommandRegistry()

        register_commands(
            self.registry,
            self.system
        )
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

        if intent["type"] == "exit":
            self.tts.speak("Hasta luego. ¡Que tengas un buen día!")
            return False
        
        if intent["type"] == "command":
            result = self.registry.execute(
                intent["name"],
                intent.get("args", {})
            )

            self.tts.speak(result.response)

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