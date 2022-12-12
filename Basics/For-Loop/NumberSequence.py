import sys

maxNumb = -sys.maxsize
minNumb = sys.maxsize

n = int(input())

for i in range(0, n):
    numb = int(input())
    if numb < minNumb:
        minNumb = numb
    if numb > maxNumb:
        maxNumb = numb
print(f"Max number: {maxNumb}")
print(f"Min number: {minNumb}")
