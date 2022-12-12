book = input()
counter = 0
flag = False
text = input()
while text != "No More Books":
    if text == book:
        print(f"You checked {counter} books and found it.")
        flag = False
        break
    counter += 1
    flag = True
    text = input()

if flag:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")