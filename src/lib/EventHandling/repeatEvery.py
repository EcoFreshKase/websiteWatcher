import threading
import time

def repeatEvery(interval_ms: int):
    """Decorator that repeats the decorated function at a specified interval.
    The function will be executed non blocking in a separate thread.

    Args:
        interval_ms (int): The interval in milliseconds at which the decorated function should be repeated.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            def loop():
                while True:
                    func(*args, **kwargs)
                    time.sleep(interval_ms / 1000.0)  # Convert milliseconds to seconds

            thread = threading.Thread(target=loop)

            # Set the thread as a daemon so it won't prevent the program from exiting
            thread.daemon = True
            thread.start()

        return wrapper
    return decorator
