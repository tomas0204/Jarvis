import os 
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY no está configurada")

STT_LANGUAGE = "es-AR"

STT_TIMEOUT = 7

STT_PHRASE_TIME_LIMIT = 16

TTS_RATE = 180

TTS_VOLUME = 1.0

TTS_VOICE = "Sabina"

LLM_MODEL = "openai/gpt-oss-20b"

LLM_SYSTEM_PROMPT = """
Eres JARVIS, un asistente virtual inteligente servicial.
Responde de forma clara, precisa y profesional.
Tu personalidad es educada, tranquila y ligeramente sofisticada.
Tus respuestas deben ser concisas y directas, evitando redundancias ni palabras de más al momento de respuestas simples.
"""

LLM_MAX_HISTORY = 10

APPLICATIONS = {
    "chrome": {
        "type": "path",
        "value": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    },

    "steam": {
        "type": "path",
        "value": r"C:\Program Files (x86)\Steam\steam.exe"
    },
    
    "discord": {
        "type": "path",
        "value": r"C:\Users\tomas\AppData\Local\Discord\app-1.0.9255\Discord.exe"
    },
    
    "code": {
        "type": "path",
        "value": r"C:\Users\tomas\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    },
    
    "overwatch": {
        "type": "path",
        "value": r"D:\SteamLibrary\steamapps\common\Overwatch\Overwatch.exe"
    },
    
    "spotify": {
        "type": "uri",
        "value": "spotify:"
    },
}
WEBSITES = {
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chatgpt.com",
    "verde": "https://kick.com",
    "twitch": "https://www.twitch.tv",
    "netflix": "https://www.netflix.com",
    "whatsapp": "https://web.whatsapp.com",
}

SEARCH_URLS = {
    "youtube": "https://www.youtube.com/results?search_query={query}",
    "github": "https://github.com/search?q={query}",
    "google": "https://www.google.com/search?q={query}",
    "twitch": "https://www.twitch.tv/search?term={query}",
    "reddit": "https://www.reddit.com/search/?q={query}",
}

WEATHER_LATITUDE = -26.732
WEATHER_LONGITUDE = -65.259
WEATHER_LOCATION = "Tafí Viejo, Tucumán"