time_first = int(input())
time_sec = int(input())
time_third = int(input())

time = time_first + time_sec + time_third

minutes = time // 60
seconds = time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")