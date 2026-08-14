from voice.speech_to_text import SpeechToText

stt = SpeechToText()

stt.calibrate()

audio = stt.listen()
text = stt.transcribe(audio)

print(f"Has dicho: {text}")