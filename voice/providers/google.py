import speech_recognition   as sr
from utils.logger           import logger
from config                 import (
    STT_LANGUAGE,
)

class GoogleSTT:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def transcribe(self, audio):
        try:
            return self.recognizer.recognize_google(audio, language=STT_LANGUAGE)
        except sr.UnknownValueError:
            logger.warning("No se pudo interpretar el audio.")
            return None
        except sr.RequestError:
            logger.error("Error al comunicarse con el servicio de reconocimiento.")
            return None