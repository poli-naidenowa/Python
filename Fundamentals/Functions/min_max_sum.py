txt = input().split()
numbers = sorted([int(n) for n in txt])

print(f"The minimum number is {numbers[0]}")
print(f"The maximum number is {numbers[-1]}")
print(f"The sum number is: {sum(numbers)}")