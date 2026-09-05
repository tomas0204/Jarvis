from voice.speech_to_text import SpeechToText

stt = SpeechToText()

stt.calibrate()

while True:
    audio = stt.listen()

    if audio is None:
        continue

    text = stt.transcribe(audio)

    print(f"Detectado: {text}")