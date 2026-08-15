COMMAND_WORDS = [
    "abre",
    "abrir",
    "abri",
    "ejecuta",
    "ejecutar",
    "inicia",
    "iniciar"
]

class Intent: 
    
    def detect(self, text):
        text = text.lower().strip()

        if text in ["salir", "terminar", "adiós"]:
            return {
                "type": "exit",
                "name": None
            }

        if any(word in text for word in COMMAND_WORDS):
            if "chrome" in text:
                return {
                    "type": "command",
                    "name": "open_chrome"
                }

        return {
            "type": "conversation",
            "name": None
        }