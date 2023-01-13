def draw_rombus(n):
    for i in range(n):
        offset = ((n - i - 1) * ' ')
        stars = '* ' * (i + 1)
        print(f"{offset}{stars}")

    for i in range(n - 2, - 1, -1):
        offset = ((n - i - 1) * ' ')
        stars = '* ' * (i + 1)
        print(f"{offset}{stars}")


x = int(input())
draw_rombus(x)