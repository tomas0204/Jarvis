from datetime import datetime
from queue import Queue
from typing import Callable
import time


class EventBus:

    def __init__(self):
        self.listeners: list[Callable] = []

    def subscribe(self, listener: Callable):
        self.listeners.append(listener)

        return lambda: self.listeners.remove(listener)

    def emit(self, event: dict):
        for listener in self.listeners:
            listener(event)


event_bus = EventBus()
event_queue = Queue()


def emit_event(event_type: str, **data):
    event = {
        "type": event_type,
        **data
    }

    # Cola utilizada por FastAPI/WebSocket
    event_queue.put(event)

    # EventBus interno
    event_bus.emit(event)


def emit_state(state: str):
    emit_event(
        "STATE_CHANGED",
        state=state
    )


def emit_status(status: str):
    emit_event(
        "JARVIS_STATUS",
        status=status
    )


def emit_command(command: str):
    emit_event(
        "COMMAND_EXECUTED",
        command=command
    )


def create_message(sender: str, text: str):
    return {
        "id": int(time.time() * 1000),
        "sender": sender,
        "text": text,
        "timestamp": datetime.now().isoformat()
    }


def emit_user_message(text: str):
    emit_event(
        "USER_MESSAGE",
        message=create_message(
            "USER",
            text
        )
    )


def emit_jarvis_message(text: str):
    emit_event(
        "JARVIS_MESSAGE",
        message=create_message(
            "JARVIS",
            text
        )
    )

