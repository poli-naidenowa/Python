x = int(input())
y = int(input())
magic_number = int(input())
flag = True

step = 0
for i in range(x, y+1):
    for j in range(x, y+1):
        step += 1
        if i + j == magic_number:
            print(f"Combination N:{step} ({i} + {j} = {magic_number})")
            flag = False
            break
    if flag is False:
        break

if flag:
    print(f"{step} combinations - neither equals {magic_number}")