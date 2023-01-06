txt = input().split()

isTerminate = False
count_A = 11
count_B = 11

for el in txt:

    if el[0] == 'A':
        count_A -= 1
    else:
        count_B -= 1
    if count_B < 7 or count_A < 7:
        isTerminate = True
        break

print(f"Team A - {count_A}; Team B - {count_B}")
if isTerminate:
    print("Game was terminated")

