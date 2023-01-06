txt = input().split()

for i in range(len(txt)):
    txt[i] = int(txt[i]) * -1

print(txt)
