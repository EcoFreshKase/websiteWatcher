from pydispatch import dispatcher

class EventHandler:
    """
    A class that handles events by connecting its methods with the `@onEvent` decorator to signals.
    """
    def __init__(self) -> None:
        self.startEventListener()

    def startEventListener(self) -> None:
        for method_name in dir(self):
            method = getattr(self, method_name)
            if hasattr(method, '_subscribedEvents'):
                for event in method._subscribedEvents:
                    dispatcher.connect(method, signal=event)