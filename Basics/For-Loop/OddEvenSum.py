n = int(input())
sum_evens = 0
sum_odds = 0
for i in range(1, n+1):
    numb = int(input())
    if i%2 == 0:
        sum_evens += numb
    else:
        sum_odds += numb

if sum_odds == sum_evens:
    print("Yes")
    print(f"Sum = {sum_odds}")
else:
    print("No")
    print(f"Diff = {abs(sum_odds - sum_evens)}")
