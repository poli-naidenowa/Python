#pens - 5.80
#markers - 7.2
#cleenig spray - 1.20/L

pens = int(input())
markers = int(input())
cleening_spray = int(input())
discount = int(input())

result = pens * 5.80 + markers * 7.20 + cleening_spray * 1.20

end_result = result - (result * discount * 0.01)
print(end_result)
