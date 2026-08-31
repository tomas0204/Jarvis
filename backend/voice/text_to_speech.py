import asyncio
import os
import tempfile

import edge_tts
import pygame
import pyttsx3

from config import TTS_RATE, TTS_VOLUME, TTS_VOICE
from backend.utils.logger import logger


class TextToSpeech:

    VOICE = "es-MX-JorgeNeural"

    def __init__(self):
        self.engine = None

    # =========================
    # EDGE TTS
    # =========================

    def _speak_edge(self, text):
        temp_path = None

        try:
            with tempfile.NamedTemporaryFile(
                suffix=".mp3",
                delete=False
            ) as temp_file:
                temp_path = temp_file.name

            async def generate():
                communicate = edge_tts.Communicate(
                    text,
                    self.VOICE
                )

                await communicate.save(temp_path)

            asyncio.run(generate())

            pygame.mixer.init()
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            return True

        except Exception as error:
            logger.warning(
                f"Edge TTS no disponible: {error}"
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

    # =========================
    # PYTTSX3 / SABINA
    # =========================

    def _find_voice(self, name):
        try:
            voices = self.engine.getProperty("voices")

            for voice in voices:
                if name.lower() in voice.name.lower():
                    return voice.id

        except Exception as error:
            logger.error(
                f"No se pudieron obtener las voces locales: {error}"
            )

        return None

    def _speak_local(self, text):
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
                self.engine.setProperty(
                    "voice",
                    voice_id
                )

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

        # Primero intenta Alonso
        if self._speak_edge(text):
            return

        # Si Edge TTS falla, usa Sabina
        logger.warning(
            "Usando voz local como alternativa."
        )

        self._speak_local(text)