score = int(input())

bonus_score = 0
if score % 2 == 0:
    bonus_score += 1
elif score % 5 == 0 and score % 10 != 0:
    bonus_score += 2

if score <= 100:
    bonus_score += 5

elif score > 100 and score <= 1000:
    bonus_score += score * 0.2

elif score > 1000:
    bonus_score += score * 0.1

print(bonus_score)
print(bonus_score+score)