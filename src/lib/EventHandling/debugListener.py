# debug listener, prints sender and params
def debug_listener(sender, **kwargs):
    print(f"\033[33m[DEBUG]\033[0m '{sender}' sent data '{", ".join([
            f"{key} => {value}" for key, value in kwargs.items()
        ])}'"
    )