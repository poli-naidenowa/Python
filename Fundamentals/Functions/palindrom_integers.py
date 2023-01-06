def is_palindrom(n):
    return n == n[::-1]


def print_palindromes(sequance):
    for n in sequance:
       print(is_palindrom(n))


txt = input().split(", ")
print_palindromes(txt)
