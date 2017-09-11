getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
getal1 = eval(input("geef getal 1: "))
getal2 = eval(input("geef getal 2: "))
aantal = 0

for getal in getallenrij:
    if getal == getal1:
        aantal += 1
    if getal == getal2:
        aantal += 1

if aantal  == 0:
    print("het getal komt niet voor in de lijst")
elif aantal == 1:
    print("een van de getallen komt voor in lijst")
else:
    print("beide getallen komen voor in de lijst")