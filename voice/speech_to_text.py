import speech_recognition as sr

class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def calibrate(self):
        with self.microphone as source:
            print("Calibrando micrófono...")
            self.recognizer.adjust_for_ambient_noise(source)

    def listen(self):
        with self.microphone as source:
            print("Escuchando...")
            audio = self.recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=10
        )

        try:
            return self.recognizer.recognize_google(
                audio,
                language="es-AR"
            )
        except sr.UnknownValueError:
            print("No pude entenderte.")
            return None