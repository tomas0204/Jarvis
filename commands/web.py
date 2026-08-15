import webbrowser
from urllib.parse import quote
from config import SEARCH_URLS
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

    def search_website(self, name, query):
        try:
            search_url = SEARCH_URLS.get(name)

            if not search_url:
                return CommandResult(
                    False,
                    f"No puedo buscar directamente en {name}."
                )

            encoded_query = quote(query)

            url = search_url.format(query=encoded_query)

            webbrowser.open(url)

            return CommandResult(
                True,
                f"Buscando {query} en {name}."
            )

        except Exception as e:
            return CommandResult(
                False,
                f"No pude realizar la búsqueda: {e}"
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