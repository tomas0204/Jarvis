import pyttsx3
from config                 import TTS_RATE, TTS_VOICE, TTS_VOLUME
from backend.utils.logger   import logger

class TextToSpeech:

    def __init__(self):
        self.engine = None

    def _initialize_engine(self):
        try:
            self.engine = pyttsx3.init()

            self.engine.setProperty("rate", TTS_RATE)
            self.engine.setProperty("volume", TTS_VOLUME)

            voice_id = self._find_voice(TTS_VOICE)

            if voice_id:
                logger.info(f"Usando la voz '{TTS_VOICE}'")
                self.engine.setProperty("voice", voice_id)

            return True

        except Exception as error:
            logger.error(f"No se pudo inicializar TTS: {error}")
            self.engine = None
            return False

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
        if not self._initialize_engine():
            return

        try:
            self.engine.say(text)
            self.engine.runAndWait()

        except Exception as error:
            logger.error(f"Error al reproducir voz: {error}")

        finally:
            self.engine = None