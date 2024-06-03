from functools import wraps
from pydispatch import dispatcher

def emitAsEvent(signal: str):
    """
    Decorator function that emits the result of the function wrapped as an event.

    Args:
        signal (str): Signal of the event emitted.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            dispatcher.send(signal=signal, sender=args[0], result=result)
            return result
        return wrapper
    return decorator