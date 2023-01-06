def repeat_string(string, n):
    for i in range(n):
        print(string, end="")


txt = input()
times = int(input())
repeat_string(txt, times)

repeat_string2 = lambda txt, times: txt * times
print(repeat_string2)