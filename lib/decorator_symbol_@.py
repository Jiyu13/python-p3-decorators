def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper


@decorator
def get_called():
    print("I am the function and I am being called.")


get_called()


# I am the output that lets you know the function is about to be called.
# I am the function and I am being called.
# I am the output that lets you know the function has been called.