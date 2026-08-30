from config import WEBSITES, APPLICATIONS

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
    
    WAKE_WORDS = [
        "hey jarvis",
        "hola jarvis",
        "oye jarvis",
        "ok jarvis",
        "okay jarvis",
        "jarvis",
        "eu jarvis",
        "che jarvis",
        "jarvis activate"
    ]

    def is_wake_word(self, text):
        text = self._normalize_wake_word(text)

        return any(
            wake_word in text
            for wake_word in self.WAKE_WORDS
        )

    def detect(self, text):
        text = self._normalize(text)
        words = text.split()
        print(f"TEXTO RECIBIDO: {text}")
        if text in ["salir", "terminar", "adiós", "adios", "chau", "chao", "desactivate", "desactivar", "apagate", "apagar"]:
            return {
                "type": "exit",
                "name": None,
                "args": {}
            }

        # Buscar en web
        result = self._detect_search(text)

        if result:
            return result

        # Abrir sitio web
        result = self._detect_website(words)

        if result:
            return result

        # Abrir aplicaciones
        result = self._detect_application(words)

        if result:
            return result

        # Hora
        if "qué hora" in text or "que hora" in text:
            return {
                "type": "command",
                "name": "get_time",
                "args": {}
            }

        # Fecha
        if (
            "qué fecha" in text
            or "que fecha" in text
            or "qué día" in text
            or "que día" in text
            or "dia" in text
        ):
            return {
                "type": "command",
                "name": "get_date",
                "args": {}
            }

        return {
            "type": "conversation",
            "name": None,
            "args": {}
        }

    def _detect_search(self, text):
        if not text.startswith("busca "):
            return None

        query = text[6:].strip()

        if not query:
            return None

        for website in WEBSITES:

            phrase = f"en {website}"

            if phrase in query:
                search_query = query.replace(
                    phrase,
                    ""
                ).strip()

                if not search_query:
                    return None

                return {
                    "type": "command",
                    "name": "search_website",
                    "args": {
                        "name": website,
                        "query": search_query
                    }
                }

        return {
            "type": "command",
            "name": "search_website",
            "args": {
                "name": "google",
                "query": query
            }
        }

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

    def _detect_application(self, words):
        if not any(word in words for word in OPEN_WORDS):
            return None
        
        text = " ".join(words)

        for application, data in APPLICATIONS.items():
            for alias in data.get("aliases", []):
                if alias in text:
                    return {
                        "type": "command",
                        "name": "open_application",
                        "args": {
                            "name": application
                        }
                    }

        return None

    def _normalize(self, text):
        text = text.lower().strip()

        words = text.split()

        if words and words[0] == "jarvis":
            words.pop(0)

        return " ".join(words)

    def _normalize_wake_word(self, text):
        text = text.lower().strip()

        for char in ",.!?¿¡":
            text = text.replace(char, "")

        return " ".join(text.split())