import os
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not API_KEY:
    raise RuntimeError("No se encontró ELEVENLABS_API_KEY en el archivo .env")

client = ElevenLabs(api_key=API_KEY)

text = "Buenas noches. ¿En qué puedo ayudarte?"

audio = client.text_to_speech.convert(
    text=text,
    voice_id="xzwAzC56IlTLCgatb6dE",
    model_id="eleven_v3",
    output_format="mp3_44100_128",
)

output_path = Path(__file__).parent / "elevenlabs_test.mp3"

with open(output_path, "wb") as f:
    for chunk in audio:
        f.write(chunk)

print(f"Audio generado correctamente: {output_path}")