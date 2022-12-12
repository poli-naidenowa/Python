smallest = int(input())
biggest = int(input())
ostatuk = 0

for num in range(smallest, biggest + 1):
    numToString = str(num)
    sum_odds = 0
    sum_evens = 0
    for i in range(0, len(numToString)):
        if i % 2 == 0:
            sum_evens += int(numToString[i])
        else:
            sum_odds += int(numToString[i])
    if sum_odds == sum_evens:
        print(num, end=" ")


