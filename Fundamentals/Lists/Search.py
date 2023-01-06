n = int(input())
word = input()
my_list = []

for i in range(n):
    text = input()
    my_list.append(text)

print(my_list)

for i in my_list:
    if word not in i:
        my_list.remove(i)
print(my_list)