import os 
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY no está configurada")

STT_LANGUAGE = "es-AR"

STT_TIMEOUT = 5

STT_PHRASE_TIME_LIMIT = 10

TTS_RATE = 180

TTS_VOLUME = 1.0

TTS_VOICE = "Sabina"

LLM_MODEL = "llama-3.3-70b-versatile"

LLM_SYSTEM_PROMPT = """
Eres JARVIS, un asistente virtual inteligente servicial.
Responde de forma clara, precisa y profesional.
Tu personalidad es educada, tranquila y ligeramente sofisticada.
Tus respuestas deben ser concisas y directas, evitando redundancias ni palabras de más al momento de respuestas simples.
"""

LLM_MAX_HISTORY = 10