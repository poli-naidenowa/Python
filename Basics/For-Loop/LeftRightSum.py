import math

n = int(input())
n *= 2
sumRight = 0
sumLeft = 0

for i in range(0, n):
    numb = int(input())
    if i < n/2:
        sumLeft += numb
    else:
        sumRight += numb
if sumRight == sumLeft:
    print(f"Yes, sum = {sumLeft}")
else:
    print(f"No, diff = {abs(sumLeft - sumRight)}")
