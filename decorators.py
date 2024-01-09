def hello_world_decorator(callback_func):

    def inner_wrapper_func():
        print("Hello")
        callback_func()
        print("Goodnight")

    return inner_wrapper_func

def World():
    print("world")

World = hello_world_decorator(World)
World()