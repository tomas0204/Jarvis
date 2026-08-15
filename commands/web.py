import webbrowser
from urllib.parse import quote

from commands.registry import CommandResult


class WebCommands:

    def open_website(self, name, url):
        try:
            webbrowser.open(url)

            return CommandResult(
                True,
                f"Abriendo {name}."
            )

        except Exception as e:
            return CommandResult(
                False,
                f"No pude abrir {name}: {e}"
            )

    def search(self, query):
        try:
            encoded_query = quote(query)
            url = f"https://www.google.com/search?q={encoded_query}"

            webbrowser.open(url)

            return CommandResult(
                True,
                f"Buscando {query}."
            )

        except Exception as e:
            return CommandResult(
                False,
                f"No pude realizar la búsqueda: {e}"
            )