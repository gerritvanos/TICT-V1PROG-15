getallenrij = [2,4,6,8,10,9,7]
zoekgetal = eval(input("welk getal wil u zoeken:"))
gevonden = False
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = True
    else:
        gevonden = False
if gevonden == False:
    print("het getal staat in de lijst")
else:
    print("helaas het getal staat niet in de lijst")