import math

figure = input()
result = 0.0

if figure == "square":
    a = float(input())
    result = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    result = a * b
elif figure == "circle":
    r = float(input())
    result = math.pi * r * r
elif figure == "triangle":
    a = float(input())
    b = float(input())

    result =a * b/2

print(f"{result:.3f}")