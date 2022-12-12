destination = input()
saved_money = 0.0

while destination != "End":
    min_budget = float(input())
    while saved_money <= min_budget:
        money = float(input())
        saved_money += money
        if saved_money >= min_budget:
            print(f"Going to {destination}!")
            break
    saved_money = 0.0
    destination = input()
