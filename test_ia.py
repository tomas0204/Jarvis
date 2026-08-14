from ai.llm import LLM

llm = LLM()

while True:
    message = input("Tú: ")

    if message.lower() == "salir":
        break

    response = llm.ask(message)

    print(f"JARVIS: {response}")