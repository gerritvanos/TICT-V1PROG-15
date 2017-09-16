def standaardtarief (afstandKM):
    bedrag = 0
    if afstandKM>50:
        bedrag = afstandKM *0.60 +15
        return (bedrag)
    elif afstandKM>0:
        bedrag= afstandKM*0.80
        return (bedrag)
    else:
        bedrag= 0
        return (bedrag)


def ritprijs(leeftijd,weekendrit,afstandKM):
    prijs = standaardtarief(afstandKM)
    if (leeftijd < 12 or leeftijd >= 65) and weekendrit == False: #dit is de werkdagen voor ouderen en kinderen
        kortingsprijs = prijs - (prijs/100 *30)
        return (round(kortingsprijs, 2))
    elif (leeftijd < 12 or leeftijd >= 65) and weekendrit == True: #dit is het weekendtarief voor ouderen en kinderen
        kortingsprijs = prijs - (prijs / 100 * 35)
        return (round(kortingsprijs, 2))
    elif (leeftijd >= 12 or leeftijd < 65) and weekendrit == True: #andere leeftijdsgroepen in het weekend
        kortingsprijs = prijs - (prijs / 100 * 40)
        return (round(kortingsprijs, 2))
    else: #dit zijn de andere leeftijdsgroepen doordeweeks
        kortingsprijs=prijs
        return(round(kortingsprijs,2))


# dit is de input variant
leeftijd = eval(input("geef je leftijd: "))
input_weekendrit = input("is het een weekend rit(ja/nee) ")
afstandKM=eval(input("wat is de afstand van de rit: "))

if input_weekendrit == 'ja': #hier maak ik een boolean van de invoer van weeekend rit
    weekendrit = True
elif input_weekendrit == 'nee':
    weekendrit = False
else:
    print("u heeft geen geldige waarde ingevuld bij weekendrit")

print(ritprijs(leeftijd,weekendrit,afstandKM))

#hieronder volgen een aantal test opdrachten
print(ritprijs(18,False,10)) #standaardtarief voor overige leefdtijdsgroepen dus 10*0.8 (uitkomst moet zijn 8.0euro)
print(ritprijs(18,False,-10))#negatieve afstand dus prijs is 0 (uitkomst moet zijn dus 0euro)
print(ritprijs(18,False,60))#afstand groter dan 50km dus 15€+60*0.6 (antwoord moet zijn 51 euro)
print(ritprijs(10,False,10))#korting doordeweeks voor kinderen 30% (antwoord moet zijn 5.6 euro)
print(ritprijs(66,False,10))#korting doordeweeks voor ouderen 30%(antwoord moet zijn 5.6euro)
print(ritprijs(10,True,10))#korting weekend kinderen 35% (antwoord moet zijn 5.2 euro)
print(ritprijs(66,True,10))#korting weekend ouderen dus 35%(antwoord moet zijn 5.2 euro)
print(ritprijs(18,True,10))#korting weekend overig dus 40%(antwoord moet zijn 4.8 euro)