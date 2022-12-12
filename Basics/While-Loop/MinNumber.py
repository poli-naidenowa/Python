import sys

numb = sys.maxsize
text = input()

while text != "Stop":
    n = int(text)
    if n < numb:
        numb = n
    text = input()

print(numb)
