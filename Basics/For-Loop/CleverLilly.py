lili_age = int(input())
washmashine_price = float(input())
toy_price = int(input())

sum = 0
money = 10

for i in range(1, lili_age + 1):
    if i % 2 == 0:
        sum += money
        sum -= 1
        money += 10
    else:
        sum += toy_price


if sum >= washmashine_price:
    print(f"Yes! {sum - washmashine_price:.2f}")
else:
    print(f"No! {washmashine_price - sum:.2f}")

