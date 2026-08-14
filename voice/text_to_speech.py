import pyttsx3
from config import TTS_RATE, TTS_VOICE, TTS_VOLUME
from utils.logger import logger

class TextToSpeech:

    def __init__(self):
        try:
            self.engine = pyttsx3.init()
        except Exception as error:
            logger.error(f"No se pudo inicializar TTS: {error}")
            self.engine = None

        self.engine.setProperty("rate", TTS_RATE)
        self.engine.setProperty("volume", TTS_VOLUME)

        voice_id = self._find_voice(TTS_VOICE)

        if voice_id:
            logger.info(f"Usando la voz '{TTS_VOICE}'")
            self.engine.setProperty("voice", voice_id)
        else:
            logger.warning(f"La voz '{TTS_VOICE}' no se encontró")

    def _find_voice(self, name):
        try:
            voices = self.engine.getProperty("voices")

            for voice in voices:
                if name.lower() in voice.name.lower():
                    return voice.id

        except Exception as error:
            logger.error(f"No se pudieron obtener las voces: {error}")

        return None

    def speak(self, text):
        if self.engine is None:
            logger.error("TTS no está disponible.")
            return

        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as error:
            logger.error(f"Error al reproducir voz: {error}")