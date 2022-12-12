import sys

text = input()
numb = -sys.maxsize
while text != "Stop":
    n = int(text)
    if n > numb:
        numb = n
    text = input()
print(numb)