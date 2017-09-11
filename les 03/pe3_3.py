leeftijd = eval(input("geef je leeftijd: "))
paspoort = input("Nederlands paspoort (ja/nee): ")

if leeftijd >= 18 and paspoort == "ja":
    print("gefeliciteerd, je mag stemmen")
else:
    print("sorry je mag niet stemmen")