def print_even(list):
    my_list = []
    for number in list:
        if number % 2 == 0:
            my_list.append(number)
    print(my_list)


def print_odd(list):
    my_list = []
    for number in list:
        if number % 2 != 0:
            my_list.append(number)
    print(my_list)


def print_negative(list):
    my_list = []
    for number in list:
        if number < 0:
            my_list.append(number)
    print(my_list)


def print_positive(list):
    my_list = []
    for number in list:
        if number >= 0:
            my_list.append(number)
    print(my_list)


n = int(input())
my_list = []

for i in range(n):
    number = int(input())
    my_list.append(number)

choise = input()

if choise == "even":
    print_even(my_list)
elif choise == "odd":
    print_odd(my_list)
elif choise == "negative":
    print_negative(my_list)
else:
    print_positive(my_list)