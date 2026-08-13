import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="es-AR")
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
        return None