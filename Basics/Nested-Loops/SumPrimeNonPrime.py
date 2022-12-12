sum_prime = 0
sum_non_prime = 0


def is_prime(numb):

    for i in range(2, numb):
        if i != numb and i != 1:
            if numb % i == 0:
                return False
    return True


text = input()
while text != "stop":
    num = int(text)
    if num < 0:
        print("Number is negative.")
        text = input()
        continue
    if is_prime(num):
        sum_prime += num
    else:
        sum_non_prime += num
    text = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
