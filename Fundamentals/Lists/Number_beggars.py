txt = input().split(", ")
sequance = [int(n) for n in txt]
number = int(input())

if len(sequance) < number:
    while len(sequance) < number:
        sequance.append(0)
elif len(txt) > number:
    new_sequance = []
    for i in range(number):
        new_sequance.append(sum(sequance[i] for i in range(i, len(sequance), number)))
    sequance = new_sequance

print(sequance)
