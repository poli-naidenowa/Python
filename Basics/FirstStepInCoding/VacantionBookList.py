count_str = int(input())
str_per_hour = int(input())
count_days = int(input())

total_time = count_str/str_per_hour
need_time = total_time//count_days

print(int(need_time))