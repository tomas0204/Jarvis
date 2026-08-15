class Intent: 
    
    def detect(self, text):
        text = text.lower().strip()

        if text in ["salir", "terminar", "adiós"]:
            return {
                "type": "exit",
                "name": None
            }

        if "abre chrome" in text or "abrir chrome" in text:
            return {
                "type": "command",
                "name": "open_chrome"
            }

        return {
            "type": "conversation",
            "name": None
        }