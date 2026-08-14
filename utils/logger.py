import logging


logger = logging.getLogger("jarvis")

logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)