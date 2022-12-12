#Type of tickets - price
premiere = 12.00
normal = 7.5
#discount for kids and students
discount = 5

ticket_type = input()
rows = int(input())
cols = int(input())

result = rows * cols

if ticket_type == "Premiere":
    result *= premiere
elif ticket_type == "Normal":
    result *= normal
elif ticket_type == "Discount":
    result *= discount

print(f"{result:.2f} leva")