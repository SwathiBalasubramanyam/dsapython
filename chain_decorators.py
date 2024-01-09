# Write your function here.
def chain_decorator(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x * x
    return inner

def multiply_decorator(func):
    def multiply_inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return 3 * x
    return multiply_inner

@chain_decorator
@multiply_decorator
def num(a, b):
    return a + b

print(num(5, 2))  #> 441
print(num(8, 2))  #> 900
print(num(4, 9))  #> 1521