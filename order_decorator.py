
def order_decorator(func):
    
    def inner(num):
        print(1)
        x = func(num)
        print(3)
        return x

    return inner

def middle(num):
    print(num)
    return num * num