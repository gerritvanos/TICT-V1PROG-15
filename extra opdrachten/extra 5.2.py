getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
oneven = 0
deel2_3 = 0
for getal in getallenrij:
    if getal%2 > 0:
        oneven +=1

    if getal%3 == 0 and getal%2 == 0:
        deel2_3 += 1

print("het aantal even getallen is:",oneven)
print("het aantal getallen deelbaar door 2 en 3 is:",deel2_3)