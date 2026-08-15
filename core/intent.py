class Intent: 
    def detect(self, text):
        text = text.lower().strip()

        if text in ["salir", "terminar", "adiós", "chau", "hasta luego", "nos vemos", "finalizar", "cerrar", "apagar", "detener"]:
            return "exit"

        return "conversation"