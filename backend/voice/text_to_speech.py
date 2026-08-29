import os
import tempfile

import pygame
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

from backend.utils.logger import logger


load_dotenv()


class TextToSpeech:

    VOICE_ID = "bM9fxaEUB1jfSSiHrP24"
    MODEL_ID = "eleven_multilingual_v2"

    def __init__(self):
        self.client = None

    def _initialize_client(self):
        try:
            api_key = os.getenv("ELEVENLABS_API_KEY")

            if not api_key:
                logger.error("No se encontró ELEVENLABS_API_KEY")
                return False

            self.client = ElevenLabs(api_key=api_key)

            return True

        except Exception as error:
            logger.error(
                f"No se pudo inicializar ElevenLabs TTS: {error}"
            )
            self.client = None
            return False

    def speak(self, text):

        if not self._initialize_client():
            return

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

        except Exception as error:
            logger.error(f"Error al reproducir voz: {error}")

        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()

            if temp_path and os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass

            self.client = None