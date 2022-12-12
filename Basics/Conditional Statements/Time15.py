hours = int(input())
minutes = int(input())

if (minutes + 15) > 59:
    hours+= 1
    if hours == 24:
        hours = 0
    result_minutes = minutes + 15 - 60
    if result_minutes < 10:
        print(f"{hours}:0{result_minutes}")
    else:
        print(f"{hours}:{result_minutes}")
else:
    minutes +=15
    print(f"{hours}:{minutes}")