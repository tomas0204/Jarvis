import os
import tempfile

import pygame
import pyttsx3

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

from config import TTS_RATE, TTS_VOICE, TTS_VOLUME
from backend.utils.logger import logger


load_dotenv()


class TextToSpeech:

    VOICE_ID = "bM9fxaEUB1jfSSiHrP24"
    MODEL_ID = "eleven_multilingual_v2"

    def __init__(self):
        self.client = None
        self.engine = None

    # =========================
    # ELEVENLABS
    # =========================

    def _initialize_elevenlabs(self):

        try:
            api_key = os.getenv("ELEVENLABS_API_KEY")

            if not api_key:
                logger.warning(
                    "No se encontró ELEVENLABS_API_KEY."
                )
                return False

            self.client = ElevenLabs(api_key=api_key)

            return True

        except Exception as error:
            logger.error(
                f"No se pudo inicializar ElevenLabs: {error}"
            )

            self.client = None

            return False

    def _speak_elevenlabs(self, text):

        if not self._initialize_elevenlabs():
            return False

        temp_path = None

        try:

            audio = self.client.text_to_speech.convert(
                text=text,
                voice_id=self.VOICE_ID,
                model_id=self.MODEL_ID,
                output_format="mp3_44100_128",
            )

            audio_data = b"".join(audio)

            with tempfile.NamedTemporaryFile(
                suffix=".mp3",
                delete=False
            ) as temp_file:

                temp_file.write(audio_data)
                temp_path = temp_file.name

            pygame.mixer.init()
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            return True

        except Exception as error:

            logger.warning(
                f"ElevenLabs no disponible: {error}"
            )

            return False

        finally:

            try:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            except Exception:
                pass

            if temp_path and os.path.exists(temp_path):

                try:
                    os.remove(temp_path)
                except OSError:
                    pass

            self.client = None

    # =========================
    # PYTTSX3 FALLBACK
    # =========================

    def _initialize_local_tts(self):

        try:

            self.engine = pyttsx3.init()

            self.engine.setProperty(
                "rate",
                TTS_RATE
            )

            self.engine.setProperty(
                "volume",
                TTS_VOLUME
            )

            voice_id = self._find_voice(TTS_VOICE)

            if voice_id:

                logger.info(
                    f"Usando voz local '{TTS_VOICE}'"
                )

                self.engine.setProperty(
                    "voice",
                    voice_id
                )

            return True

        except Exception as error:

            logger.error(
                f"No se pudo inicializar TTS local: {error}"
            )

            self.engine = None

            return False

    def _find_voice(self, name):

        try:

            voices = self.engine.getProperty(
                "voices"
            )

            for voice in voices:

                if name.lower() in voice.name.lower():

                    return voice.id

        except Exception as error:

            logger.error(
                f"No se pudieron obtener las voces locales: {error}"
            )

        return None

    def _speak_local(self, text):

        if not self._initialize_local_tts():
            return False

        try:

            self.engine.say(text)
            self.engine.runAndWait()

            return True

        except Exception as error:

            logger.error(
                f"Error al reproducir TTS local: {error}"
            )

            return False

        finally:

            self.engine = None

    # =========================
    # PUBLIC
    # =========================

    def speak(self, text):

        if self._speak_elevenlabs(text):
            return

        logger.warning(
            "Usando TTS local como alternativa."
        )

        self._speak_local(text)