name = input()
n = 0
average = 0.0
chanse = 0
while chanse < 2 and n < 12:
   grade = float(input())
   if grade < 4.00:
       chanse += 1
   average += grade
   n += 1

if chanse == 2:
    print(f"{name} has been excluded at {n-1} grade")
else:
    average /= 12
    print(f"{name} graduated. Average grade: {average:.2f}")