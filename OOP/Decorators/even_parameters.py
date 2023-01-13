def even_parameters(func):
    def wrapper(*args):
        l = list(args)
        for i in l:
            if not isinstance(i, int):
                return "Please use only even numbers!"
            if i % 2 != 0:
                return "Please use only even numbers!"
            return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(add(2, 4))
print(add("Peter", 1))

print(multiply(2, 4, 9, 8))
print(multiply(2, 4, 6, 8))
