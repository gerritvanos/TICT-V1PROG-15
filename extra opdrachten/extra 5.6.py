getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
min = 1000
max=0
for getal in getallenrij:
    if getal >max:
        max = getal
    if getal <min:
        min = getal

print("het grootste getal is",max)
print("het kleinste getal is",min)