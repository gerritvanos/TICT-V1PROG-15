def seizoen(maand):
    if maand == 12 or (maand >=1 and maand <3):
        return ("Winter")
    elif maand >=3 and maand <=5:
        return ("Lente")
    elif maand >5 and maand <=8:
        return ('Zomer')
    elif maand >=9 and maand <=11:
        return ("herfst")


maandnummer = eval(input("geef een maandnummer op: "))

print("deze maand valt in het seizoen: {}".format(seizoen(maandnummer)))