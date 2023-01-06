txt = input().split()
numbers = [int(n) for n in txt]
result = list(filter(lambda n: n % 2 == 0, numbers))

print(result)