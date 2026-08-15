COMMAND_WORDS = [
    "abre",
    "abrir",
    "abri",
    "abrí",
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
            if "chrome" in text or "navegador" in text:
                return {
                    "type": "command",
                    "name": "open_chrome"
                }
            
            if "steam" in text or "juego" in text:
                return {
                    "type": "command",
                    "name": "open_steam"
                }
            
        
        if "hora" in text or "tiempo" in text:
            return {
                "type": "command",
                "name": "get_time"
            }   

        if "fecha" in text or "dia" in text or "día" in text:
            return {
                "type": "command",
                "name": "get_date"
            }

        return {
            "type": "conversation",
            "name": None
        }