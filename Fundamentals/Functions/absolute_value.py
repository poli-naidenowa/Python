def txt_in_numbers(txt):
    numbers = [abs(float(n)) for n in txt]
    return numbers


txt = input().split()
print(txt_in_numbers(txt))
