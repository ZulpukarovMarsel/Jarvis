from commands.jarvis import jarvis_main, activate_jarvis

def hello(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            func(*args, **kwargs)
            wrapper.has_run = True

    wrapper.has_run = False
    return wrapper


@hello
def my_function():
    activate_jarvis()


if __name__ == "main":
    my_function()
    jarvis_main()
