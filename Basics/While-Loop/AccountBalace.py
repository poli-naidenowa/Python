text = input()
total = 0.0
while text != "NoMoreMoney":
    sum = float(text)
    if sum < 0:
        print("Invalid operation!")
        break;
    total += sum
    print(f"Increase: {sum:.2f}")
    text = input()
print(f"Total: {total:.2f}")