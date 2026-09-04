import base64
import io
import re

from PIL import ImageGrab
from groq import Groq

from config import GROQ_API_KEY, VISION_MODEL


def capture_screen():
    """
    Captura la pantalla principal y devuelve la imagen en memoria.
    No guarda ningún archivo en el disco.
    """

    screenshot = ImageGrab.grab()

    buffer = io.BytesIO()
    screenshot.save(
        buffer,
        format="JPEG",
        quality=85
    )

    return buffer.getvalue()


def image_to_base64(image_bytes):
    """
    Convierte los bytes de la imagen a Base64.
    """

    return base64.b64encode(image_bytes).decode("utf-8")


def clean_response(response):
    """
    Elimina el bloque de razonamiento <think>...</think>
    de la respuesta del modelo.
    """

    if not response:
        return None

    response = re.sub(
        r"<think>.*?</think>",
        "",
        response,
        flags=re.DOTALL
    )

    return response.strip()


def analyze_screen(image_bytes):
    """
    Envía una captura de pantalla a Groq Vision
    y devuelve su análisis.
    """

    client = Groq(api_key=GROQ_API_KEY)

    image_base64 = image_to_base64(image_bytes)

    response = client.chat.completions.create(
        model=VISION_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Describe la imagen que aparece en pantalla."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        },
                    },
                ],
            }
        ],
        temperature=0.7,
        max_completion_tokens=500,
    )

    result = response.choices[0].message.content

    return clean_response(result)