"""
Write a program that receives two numbers (factor and count). It should create a list with a length of the given count
 that contains only integer numbers, which are multiples of the given factor. The numbers should be only positive,
  and they should be arranged in ascending order, starting from the value of the factor.
"""

n = int(input())
size = int(input())
numbers = []
res = n
for number in range(size):
    numbers.append(res)
    res += n
print(numbers)