n = int(input())
current = 0
isEquel = False
for row in range(1, n+1):
    for col in range(1, row + 1):
        current += 1
        print(current, end=" ")
        if current == n:
            isEquel = True
            break
    print()
    if isEquel:
        break
