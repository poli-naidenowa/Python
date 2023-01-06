def sum_numbers(a, b):
    return a + b


def subtract(x, y):
    return x - y


def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a,b), c)


numb1 = int(input())
numb2 = int(input())
numb3 = int(input())

print(add_and_subtract(numb1, numb2, numb3))