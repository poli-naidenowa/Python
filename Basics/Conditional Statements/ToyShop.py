puzzle_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

#input
travel_price = float(input())
pizzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

count_toys = pizzles + dolls + bears + minions + trucks
discount = 0.0
income = pizzles * puzzle_price + dolls * doll_price + bears * bear_price + minions * minion_price + trucks * truck_price

if count_toys >= 50:
    discount = 0.25
    income = income - (income * discount)

rent = 0.1
income = income - (income * rent)

if income - travel_price >= 0:
    print(f"Yes! {(income - travel_price):.2f} lv left.")
else:
    print(f"Not enough money! {travel_price - income:.2f} lv needed.")

