from backend.ai.vision import Vision


def main():
    print("=" * 50)
    print(" JARVIS - PRUEBA DE VISIÓN")
    print("=" * 50)

    try:
        vision = Vision()

        print("Capturando pantalla...")
        respuesta = vision.analyze_screen()

        print("\nRespuesta de Jarvis:")
        print("-" * 50)
        print(respuesta)
        print("-" * 50)

    except Exception as e:
        print("\nERROR:")
        print(e)


if __name__ == "__main__":
    main()