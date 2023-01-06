def add_people(my_list, people):
    my_list[len(my_list)-1] += people


def insert_people(my_list, index, people):
    my_list[index] += people


def leave_people(my_list, index, people):
    my_list[index] -= people


n = int(input())
train = [0] * n
txt = input()

while txt != "End":
    data = txt.split()
    if len(data) < 3:
        add_people(train, int(data[1]))
    elif data[0] == "insert":
        insert_people(train, int(data[1]), int(data[2]))
    elif data[0] == "leave":
        leave_people(train, int(data[1]), int(data[2]))
    txt = input()

print(train)