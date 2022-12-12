n = int(input())
max_numb = 0
sum = 0

for i in range(0,n):
    numb = int(input())
    if numb > max_numb:
        max_numb = numb
    sum += numb

sum -= max_numb
if sum == max_numb:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(max_numb - sum)}")