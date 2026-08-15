class Intent: 
    
    def detect(self, text):
        text = text.lower().strip()

        if text in ["salir", "terminar", "adiós"]:
            return "exit"

        if "abre chrome" in text or "abrir chrome" in text:
            return "open_chrome"

        return "conversation"