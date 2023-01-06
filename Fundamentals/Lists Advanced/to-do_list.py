txt = input()
data = []
while txt != "End":
    data.append(txt)
    txt = input()

data.sort()
data = [x[2::] for x in data]
print(data)
