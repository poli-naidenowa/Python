def min_between_two(x, y):
    if x > y:
        return y
    return x


def find_min_between_three(x, y, z):
    min_x_y = min_between_two(x, y)
    min_x_z = min_between_two(x, z)
    if min_x_z < min_x_y:
        return min_x_z
    return min_x_y


a = int(input())
b = int(input())
c = int(input())
print(find_min_between_three(a, b, c))
