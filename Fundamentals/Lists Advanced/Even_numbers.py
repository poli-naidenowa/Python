"""
Write a program that reads a single string with numbers separated
by comma and space ", ".
Print the indices of all even numbers.
"""

numbers = list(map(int, input().split(", ")))
indexes = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))

even_indexes = list(filter(lambda n: n != 'no', indexes))
print(even_indexes)
