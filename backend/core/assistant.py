from threading import Event

from backend.commands.setup import register_commands
from backend.voice.speech_to_text import SpeechToText
from backend.voice.text_to_speech import TextToSpeech
from backend.ai.llm import LLM
from backend.core.intent import Intent
from backend.commands.system import SystemCommands
from backend.commands.registry import CommandRegistry

from backend.core.event_bus import (
    emit_state,
    emit_status,
    emit_command,
    emit_user_message,
    emit_jarvis_message
)


class Assistant:

    def __init__(self):
        # Control del thread principal
        self.running = Event()
        self.running.set()

        # Estado de Jarvis
        self.online = False
        self.state = "IDLE"

        # Servicios
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.llm = LLM()
        self.intent = Intent()

        # Sistema de comandos
        self.system = SystemCommands()
        self.registry = CommandRegistry()

        register_commands(
            self.registry,
            self.system
        )

    # =========================
    # ESTADO DE JARVIS
    # =========================

    def activate(self):
        self.online = True
        emit_status("ONLINE")

    def deactivate(self):
        self.online = False
        emit_status("OFFLINE")

    def set_state(self, state):
        self.state = state
        emit_state(state)

    # =========================
    # VOZ
    # =========================

    def listen(self):
        audio = self.stt.listen()

        if audio is None:
            return None

        return self.stt.transcribe(audio)

    def speak(self, text):
        self.set_state("SPEAKING")

        self.tts.speak(text)

        emit_jarvis_message(text)

        self.set_state("IDLE")

    # =========================
    # PROCESAMIENTO
    # =========================

    def process(self, text, source="voice"):

        if source == "voice":
            self.set_state("PROCESSING")
            emit_user_message(text)

        intent = self.intent.detect(text)

        if intent["type"] == "exit":
            return self._handle_exit()

        if intent["type"] == "command":
            return self._handle_command(intent)

        return self._handle_conversation(text)

    def _handle_exit(self):
        self.deactivate()

        response = "De acuerdo. Estaré esperando."

        self.speak(response)

        return {
            "type": "deactivate",
            "response": response
        }

    def _handle_command(self, intent):
        result = self.registry.execute(
            intent["name"],
            intent.get("args", {})
        )

        emit_command(intent["name"])

        response = result.response

        self.speak(response)

        return {
            "type": "command",
            "response": response,
            "command": intent["name"]
        }

    def _handle_conversation(self, text):
        response = self.llm.ask(text)

        self.speak(response)

        return {
            "type": "conversation",
            "response": response
        }

    # =========================
    # CICLO DE VOZ
    # =========================

    def run_once(self):

        self.set_state("LISTENING")

        text = self.listen()

        # El thread fue detenido mientras escuchaba
        if not self.running.is_set():
            self.set_state("IDLE")
            return

        if not text:
            self.set_state("IDLE")
            return

        # Jarvis está apagado:
        # solamente busca la wake word
        if not self.online:
            self._handle_wake_word(text)
            return

        self.process(
            text,
            source="voice"
        )

    def _handle_wake_word(self, text):

        if not self.intent.is_wake_word(text):
            self.set_state("IDLE")
            return

        self.activate()

        self.speak(
            "Sí, te escucho."
        )

    # =========================
    # CONTROL DEL THREAD
    # =========================

    def stop(self):
        print("Deteniendo Assistant...")
        self.running.clear()

    def run(self):

        self.stt.calibrate()

        while self.running.is_set():
            self.run_once()

