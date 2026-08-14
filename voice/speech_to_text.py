import speech_recognition as sr
from voice.providers.google import GoogleSTT

class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.provider = GoogleSTT()

    def calibrate(self):
        with self.microphone as source:
            print("Calibrando micrófono...")
            self.recognizer.adjust_for_ambient_noise(source)

    def listen(self):
        with self.microphone as source:
            print("Escuchando...")

            try:
                return self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )
            except sr.WaitTimeoutError:
                print("No detecté ninguna voz.")
                return None

    def transcribe(self, audio):
        if audio is None:
            return None
        
        return self.provider.transcribe(audio)