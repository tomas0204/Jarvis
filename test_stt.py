from voice.speech_to_text import SpeechToText

stt = SpeechToText()

stt.calibrate()

text = stt.listen()

print(f"Has dicho: {text}")