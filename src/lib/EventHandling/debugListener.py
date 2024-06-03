# debug listener, prints sender and params
def debug_listener(sender, **kwargs):
    print(f"[DEBUG] '{sender}' sent data '{", ".join([
            f"{key} => {value}" for key, value in kwargs.items()
        ])}'"
    )