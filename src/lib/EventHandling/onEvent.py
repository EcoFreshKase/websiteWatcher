from functools import wraps
import inspect
from typing import Callable, List
from pydispatch import dispatcher

def applyArgsToFunc(func: Callable) -> tuple[List, dict]:
    """
    A decorator function to filter the arguments and keyword arguments passed to a function and only
    pass the ones that are in the function's signature. The function is only called if the enough arguments
    are passed otherwise the function is not called.

    Example:
    ```python
    @applyArgsToFunc
    def test(a, b, c):
        print(a, b, c)

    test(1, 2, 3) # Output: 1 2 3
    test(1, 2) # Output: None
    test(1, 2, 3, 4) # Output: 1 2 3
    ```

    Args:
        func (Callable): The function to be decorated.

    Returns:
        wrapper: The decorated function.

    """
    signature = inspect.signature(func)
    @wraps(func)
    def wrapper(*args, **kwargs):
        filteredArgs = [arg for arg, param in zip(args, signature.parameters.values()) if param.kind in (param.POSITIONAL_OR_KEYWORD, param.POSITIONAL_ONLY)]
        filteredKwargs = {k: v for k, v in kwargs.items() if k in signature.parameters}

        try:
            params = signature.bind(*filteredArgs, **filteredKwargs) # Check if enough arguments are passed
        except TypeError:
            pass
        else:
            return func(*params.args, **params.kwargs)
    return wrapper

def onEvent(signal: str):
    """
    Decorator function that connects a function or method to a signal event.

    The function is only called if the dispatcher sends enough arguments to the function.
    E.g. 
    ```
    @onEvent('signal') 
    def test(event: str): 
        pass
    ``` 
    will only be called if the dispatcher
    sends a signal with the event argument.

    Currently only supports functions, staticmethods and methods. classmethods might work under certain 
    circumstances but are not supported.

    Args:
        signal (str): The name of the signal event.

    Returns:
        Callable: The decorated function or method.
    """
    
    def decorator(func: Callable):
        # Check which kind of function is passed
        argFilteredFunc = applyArgsToFunc(func)
        inClass = "." in func.__qualname__

        if inClass:
            if isinstance(func, staticmethod):
                dispatcher.connect(argFilteredFunc, signal=signal)
            elif isinstance(func, classmethod):
                raise TypeError(f'Unsupported Function Type: classmethod. Make sure you use a function, staticmethod or method')
            else: # is a method

                # Method needs a self reference, therefore can not be connected to the dispatcher
                # before an instance of the class is created. Method is connected to the dispatcher
                # at initialization if the class is a subclass of EventHandler
                if not "_subscribedEvents" in func.__dict__:
                    func._subscribedEvents = {signal: True}
                else:
                    func._subscribedEvents[signal] = True

                return applyArgsToFunc(func)
        elif not inClass and inspect.isfunction(func): # is a function
            dispatcher.connect(argFilteredFunc, signal=signal)
        else:
            raise TypeError(f'Unsupported Function Type: {func.__qualname__} Make sure you use a function, staticmethod or method')
        
        return argFilteredFunc
    return decorator