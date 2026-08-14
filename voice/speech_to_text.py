import speech_recognition   as sr
from voice.providers.google import GoogleSTT
from utils.logger           import logger
from config                 import (
    STT_TIMEOUT,
    STT_PHRASE_TIME_LIMIT
)

class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.provider = GoogleSTT()

    def calibrate(self):
        with self.microphone as source:
            logger.info("Calibrando micrófono...")
            self.recognizer.adjust_for_ambient_noise(source)

    def listen(self):
        with self.microphone as source:
            logger.info("Escuchando...")

            try:
                return self.recognizer.listen(
                    source,
                    timeout=STT_TIMEOUT,
                    phrase_time_limit=STT_PHRASE_TIME_LIMIT
                )
            except sr.WaitTimeoutError:
                logger.warning("No detecté ninguna voz.")
                return None

    def transcribe(self, audio):
        if audio is None:
            return None
        
        return self.provider.transcribe(audio)