employees_happiness = list(map(int, input().split()))
n = int(input())
employees_happiness = list(map(lambda x: x * n, employees_happiness))
average_happiness = sum(employees_happiness)/len(employees_happiness)
number_of_happier = list(filter(lambda x: x >= average_happiness, employees_happiness))

if len(number_of_happier) < len(employees_happiness) / 2:
    print(f"Score: {len(number_of_happier)}/{len(employees_happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(number_of_happier)}/{len(employees_happiness)}. Employees are happy!")
