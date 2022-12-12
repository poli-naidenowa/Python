import math

record_seconds = float(input())
distance_m = float(input())
time_per_m = float(input()) #in seconds for 1 meter

water = 12.5

total_seconts = distance_m  * time_per_m
count = distance_m // 15

total_seconts += count * water


if total_seconts > record_seconds:
    
    print(f"No, he failed! He was {total_seconts - record_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_seconts:.2f} seconds.")