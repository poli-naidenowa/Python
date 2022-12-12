numb = float(input())

if numb <= 10:
    print("slow")
elif numb <= 50:
    print("average")
elif numb <= 150:
    print("fast")
elif numb <= 1000:
    print("ultra fast")
else:
    print("extremely fast")