from typing import Callable


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