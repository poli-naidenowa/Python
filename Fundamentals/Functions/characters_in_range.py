def print_characters_in_range(start, stop):

    for ch in range(ord(start) + 1, ord(stop)):
        print(chr(ch), end=" ")


a = input()
b = input()
print_characters_in_range(a,b)