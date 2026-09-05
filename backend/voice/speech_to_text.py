import speech_recognition           as sr
from backend.voice.providers.google import GoogleSTT
from backend.utils.logger           import logger
from config                         import (
    STT_TIMEOUT,
    STT_PHRASE_TIME_LIMIT
)

class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.provider = GoogleSTT(self.recognizer)

    def calibrate(self):
        with self.microphone as source:
            logger.info("Calibrando micrófono...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def listen(self):
        with self.microphone as source:
            logger.info("Escuchando...")

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=STT_TIMEOUT,
                    phrase_time_limit=STT_PHRASE_TIME_LIMIT
                )

                return audio
            except sr.WaitTimeoutError:
                logger.warning("No detecté ninguna voz.")
                return None

    def transcribe(self, audio):
        if audio is None:
            return None
        
        return self.provider.transcribe(audio)