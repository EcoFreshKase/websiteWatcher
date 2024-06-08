from functools import wraps
from pydispatch import dispatcher

def emitAsEvent(signal: str):
    """
    Decorator function that emits the result of the function wrapped as an event.

    The decorator is meant to be used on methods of classes. The first argument of the method should be the class itself.
    Raises a TypeError if the first argument is not a class.

    Args:
        signal (str): Signal of the event emitted.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sender = func
            if args and isinstance(args[0], object):
                sender = args[0]
            result = func(*args, **kwargs)
            dispatcher.send(signal=signal, sender=sender, event=result)
            return result
        return wrapper
    return decorator