import base64
import io
import re
from PIL                        import ImageGrab
from groq                       import Groq
from backend.commands.registry  import CommandResult
from config                     import GROQ_API_KEY, VISION_MODEL

class Vision:
    
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
    
    def capture_screen(self):
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


    def image_to_base64(self, image_bytes):
        """
        Convierte los bytes de la imagen a Base64.
        """

        return base64.b64encode(image_bytes).decode("utf-8")


    def clean_response(self, response):
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


    def analyze_screen(self, image_bytes=None):
        """
        Envía una captura de pantalla a Groq Vision
        y devuelve un CommandResult.
        """

        if image_bytes is None:
            image_bytes = self.capture_screen()

        image_base64 = self.image_to_base64(image_bytes)

        try:
            response = self.client.chat.completions.create(
                model=VISION_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": (
                                    "Analiza la pantalla y responde únicamente con una descripción "
                                    "breve y clara de lo que está viendo el usuario. "
                                    "No muestres razonamiento ni etiquetas <think>."
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

            response_text = self.clean_response(
                response.choices[0].message.content
            )

            if not response_text:
                return CommandResult(
                    False,
                    "No pude obtener un análisis de la pantalla."
                )

            return CommandResult(
                True,
                response_text
            )

        except Exception as e:
            return CommandResult(
                False,
                f"No pude analizar la pantalla: {e}"
            )