import speech_recognition as sr

class GoogleSTT:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def transcribe(self, audio):
        try:
            return self.recognizer.recognize_google(audio, language="es-AR")
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None