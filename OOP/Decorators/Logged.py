from functools import wraps


def logged(funct):
    def wrapper(*args):
        result = funct(*args)
        return f"you called {funct.__name__}{args}\nit return {result}"
    return wrapper

@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
print(func(4, 4, 4))

