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
        self.online = False
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
    
    def activate(self):
        self.online = True

        event_queue.put({
            "type": "JARVIS_STATUS",
            "status": "ONLINE"
        })
    
    def deactivate(self):
        self.online = False

        event_queue.put({
            "type": "JARVIS_STATUS",
            "status": "OFFLINE"
        })

    def set_state(self, state):
        self.state = state
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

            self.deactivate()

            response = "De acuerdo. Estaré esperando."

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
                "type": "deactivate",
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

        # Jarvis está apagado: solamente busca la wake word
        if not self.online:

            if self.intent.is_wake_word(text):

                self.activate()

                self.set_state("SPEAKING")

                response = "Sí, te escucho."

                self.tts.speak(response)

                event_queue.put({
                    "type": "JARVIS_MESSAGE",
                    "message": create_message(
                        "JARVIS",
                        response
                    )
                })

                self.set_state("IDLE")

            else:
                self.set_state("IDLE")

            return True

        result = self.process(
            text,
            source="voice"
        )

        return True and result

    def run(self):
        self.stt.calibrate()

        while self.run_once():
            pass