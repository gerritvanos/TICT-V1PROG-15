def pay(hours,wage):
    loon = 0
    if hours <= 40:
        loon = hours*wage
    else:
        loon = 40*wage
        overwerk = (hours-40)*1.5*wage
        loon = loon+overwerk
    return loon
uren = eval(input("voor het aantal uren in: "))
tarief = eval(input("voer het uurloon in: "))

print(pay(uren,tarief))