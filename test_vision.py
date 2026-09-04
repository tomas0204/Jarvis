import base64
import io

from PIL import ImageGrab
from groq import Groq

from config import GROQ_API_KEY


# Modelo de Groq con capacidad de visión
VISION_MODEL = "qwen/qwen3.6-27b"


def capture_screen():
    """
    Captura la pantalla principal y devuelve la imagen en memoria.
    No guarda ningún archivo en el disco.
    """
    print("Capturando pantalla...")

    screenshot = ImageGrab.grab()

    # Convertimos la captura a JPEG en memoria
    buffer = io.BytesIO()
    screenshot.save(buffer, format="JPEG", quality=85)

    return buffer.getvalue()


def image_to_base64(image_bytes):
    """
    Convierte los bytes de la imagen a Base64.
    """
    return base64.b64encode(image_bytes).decode("utf-8")


def analyze_screen(image_bytes):
    """
    Envía la captura a Groq y solicita un análisis de la pantalla.
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
                            "Analiza el código que aparece en pantalla. "
                            "Indica qué lenguaje de programación es, "
                            "qué función o parte del programa estoy viendo "
                            "y explica brevemente qué hace ese código. "
                            "Responde en español y sé conciso."
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

    return response.choices[0].message.content


def main():
    print("=" * 50)
    print(" JARVIS - PRUEBA DE VISIÓN")
    print("=" * 50)

    try:
        # 1. Capturar pantalla
        image_bytes = capture_screen()

        print("Captura realizada correctamente.")

        # 2. Analizar con Groq
        print("Enviando captura a Groq...")
        print()

        result = analyze_screen(image_bytes)

        print("Respuesta de Groq:")
        print("-" * 50)
        print(result)
        print("-" * 50)

    except Exception as e:
        print()
        print("ERROR:")
        print(e)


if __name__ == "__main__":
    main()