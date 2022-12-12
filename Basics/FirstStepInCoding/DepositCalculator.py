sum = float(input())
months = int(input())
percent = float(input())

result = sum + months * ((sum * percent * 0.01)/12)
print(result)