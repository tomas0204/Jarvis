from backend.commands.setup         import register_commands
from backend.voice.speech_to_text   import SpeechToText
from backend.voice.text_to_speech   import TextToSpeech
from backend.ai.llm                 import LLM
from backend.core.intent            import Intent
from backend.commands.system        import SystemCommands
from backend.commands.registry      import CommandRegistry
from backend.core.event_bus         import event_queue
from datetime                       import datetime
import time


def create_message(sender, text):
    return {
        "id": int(time.time() * 1000),
        "sender": sender,
        "text": text,
        "timestamp": datetime.now().isoformat()
    }


class Assistant:

    def __init__(self):
        self.stt = SpeechToText()

        self.system = SystemCommands()
        self.registry = CommandRegistry()

        register_commands(
            self.registry,
            self.system
        )

        self.tts = TextToSpeech()
        self.llm = LLM()
        self.intent = Intent()

        self.state = "IDLE"

    def set_state(self, state):
        self.state = state
        print(f"[STATE] {state}")
        event_queue.put({
            "type": "STATE_CHANGED",
            "state": state
        })

    def listen(self):
        audio = self.stt.listen()

        if audio is None:
            return None

        return self.stt.transcribe(audio)

    def process(self, text, source="voice"):

        if source == "voice":
            self.set_state("PROCESSING")

            event_queue.put({
                "type": "USER_MESSAGE",
                "message": create_message("USER", text)
            })

        intent = self.intent.detect(text)

        if intent["type"] == "exit":

            response = "Hasta luego. ¡Que tengas un buen día!"

            self.set_state("SPEAKING")
            self.tts.speak(response)

            if source == "voice":
                event_queue.put({
                    "type": "JARVIS_MESSAGE",
                    "message": create_message(
                        "JARVIS",
                        response
                    )
                })

                self.set_state("IDLE")

            return {
                "type": "exit",
                "response": response
            }

        if intent["type"] == "command":

            result = self.registry.execute(
                intent["name"],
                intent.get("args", {})
            )

            if source == "voice":
                event_queue.put({
                    "type": "COMMAND_EXECUTED",
                    "command": intent["name"]
                })

            self.set_state("SPEAKING")
            self.tts.speak(result.response)

            if source == "voice":
                event_queue.put({
                    "type": "JARVIS_MESSAGE",
                    "message": create_message(
                        "JARVIS",
                        result.response
                    )
                })

                self.set_state("IDLE")

            return {
                "type": "command",
                "response": result.response,
                "command": intent["name"]
            }

        response = self.llm.ask(text)

        self.set_state("SPEAKING")
        self.tts.speak(response)

        if source == "voice":
            event_queue.put({
                "type": "JARVIS_MESSAGE",
                "message": create_message(
                    "JARVIS",
                    response
                )
            })

            self.set_state("IDLE")

        return {
            "type": "conversation",
            "response": response
        }

    def run_once(self):

        self.set_state("LISTENING")

        text = self.listen()

        if not text:
            self.set_state("IDLE")
            return True

        result = self.process(
            text,
            source="voice"
        )

        return result["type"] != "exit"

    def run(self):
        self.stt.calibrate()

        while self.run_once():
            pass