getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
minoneven = 1000
maxeven = 0

for getal in getallenrij:
    if getal%2 == 0 and getal>maxeven:
        maxeven=getal
    elif getal<minoneven:
        minoneven=getal

print("het minimum van de onevengetallen is",minoneven)
print("het maximum van de even getallen is",maxeven)

