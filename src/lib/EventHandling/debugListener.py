from .onEvent import onEvent
from pydispatch import dispatcher

# debug listener, prints sender and params
@onEvent(dispatcher.Any)
def debug_listener(sender, signal, event):
    print(f"\033[33m[DEBUG]\033[0m '{sender}' sent event={signal}:   {event}"
    )