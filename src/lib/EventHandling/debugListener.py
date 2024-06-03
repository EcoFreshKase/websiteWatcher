# debug listener, prints sender and params
def debug_listener(sender, **kwargs):
    print(f"\033[33m[DEBUG]\033[0m '{sender}' sent event \n\t{{\n\t\t{",\n\t\t".join([
            f"{key} => {value}" for key, value in kwargs.items()
        ])} \n\t}}"
    )