from voice.speech_to_text import SpeechToText
from utils.logger import logger


stt = SpeechToText()

stt.calibrate()

while True:
    audio = stt.listen()

    text = stt.transcribe(audio)

    if text is None:
        continue

    logger.info(f"Usuario: {text}")

    if text.lower() == "salir":
        logger.info("Deteniendo JARVIS...")
        break