budjet = float(input())
statist = int(input())
dress_price_preson = float(input())

decor_price = budjet * 0.1
money_for_dress = statist * dress_price_preson

if statist > 150:
    money_for_dress = money_for_dress - (money_for_dress * 0.1)

total = decor_price + money_for_dress

if total > budjet:
    print("Not enough money!")
    print(f"Wingard needs {total - budjet:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budjet - total:.2f} leva left.")