plastic = int(input())
paint = int(input())
razreditel = int(input())
hours_needed = int(input())

paint += paint * 0.10
sum = (plastic + 2) * 1.50 + paint * 14.50 + razreditel * 5.00 + 0.40

total = sum + (sum * 0.30 * hours_needed)
print(total)