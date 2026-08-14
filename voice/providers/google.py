import speech_recognition as sr
from config import (
    STT_LANGUAGE,
)

class GoogleSTT:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def transcribe(self, audio):
        try:
            return self.recognizer.recognize_google(audio, language=STT_LANGUAGE)
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None