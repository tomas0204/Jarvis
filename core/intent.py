from config import WEBSITES

OPEN_WORDS = [
    "abre",
    "abrir",
    "abri",
    "abrí",
    "ejecuta",
    "ejecutar",
    "inicia",
    "iniciar",
    "ve",
    "ir",
    "entra",
    "entrar"
]

class Intent:
    
    def _detect_website(self, words):
        if not any(word in words for word in OPEN_WORDS):
            return None

        for website, url in WEBSITES.items():
            if website in words:
                return {
                    "type": "command",
                    "name": "open_website",
                    "args": {
                        "name": website,
                        "url": url
                    }
                }

        return None

    def detect(self, text):
        text = self._normalize(text)
        words = text.split()

        if text in ["salir", "terminar", "adiós"]:
            return {
                "type": "exit",
                "name": None,
                "args": {}
            }
            
        result = self._detect_website(words)
        
        if result:
            return result

        if any(word in words for word in OPEN_WORDS):

            if "chrome" in words or "navegador" in words:
                return {
                    "type": "command",
                    "name": "open_chrome",
                    "args": {}
                }

            if "steam" in words or "juego" in words:
                return {
                    "type": "command",
                    "name": "open_steam",
                    "args": {}
                }

        if "qué hora" in text or "que hora" in text:
            return {
                "type": "command",
                "name": "get_time",
                "args": {}
            }

        if (
            "qué fecha" in text
            or "que fecha" in text
            or "qué día" in text
            or "que día" in text
        ):
            return {
                "type": "command",
                "name": "get_date",
                "args": {}
            }

        if any(word in words for word in OPEN_WORDS):

            for website, url in WEBSITES.items():

                if website in words:
                    return {
                        "type": "command",
                        "name": "open_website",
                        "args": {
                            "name": website,
                            "url": url
                        }
                    }

        return {
            "type": "unknown",
            "name": None,
            "args": {}
        }

    def _normalize(self, text):
        text = text.lower().strip()

        words = text.split()

        if words and words[0] == "jarvis":
            words.pop(0)

        return " ".join(words)