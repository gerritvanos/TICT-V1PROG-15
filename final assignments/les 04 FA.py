def standaardtarief (afstandKM):#deze functie berekent het standaard bedrag aan de hand van het aantal KM
    bedrag = 0.0
    if afstandKM>50: #afstand groter dan 50KM
        bedrag = afstandKM *0.60 +15
        return (bedrag)
    elif afstandKM>0: #afstand tussen 0 en 50KM
        bedrag= afstandKM*0.80
        return (bedrag)
    else:#bij negatieve afstanden wordt er 0 teruggegeven
        bedrag= 0
        return (bedrag)

def ritprijs(leeftijd,weekendrit,afstandKM): #deze functie berkent de korting
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
        return(round(kortingsprijs,))

def test(): #hiermee kan de gebruiker kiezen of hij/zij een aantal testwardes wil gebruiken of zelf iets in wil voeren
    test = input('wil u gebruik maken van de ingebouwde testfunctie?(ja/nee): ')
    if test == 'ja':
        #hieronder volgen een aantal test opdrachten (bij het uivoeren van deze test zijn van alle functies elke mogelijkheid getest
        #positieve afstanden <50km:
        print('positieve afstanden <50km:')
        print(ritprijs(64, False, 10))  #overig doordeweeks (uitkomst is 8)
        print(ritprijs(11, False, 10))  #kinderen doordeweeks(uitkomst is 5.6)
        print(ritprijs(12, False, 10))  #overig doordeweeks (uitkomst is 8)
        print(ritprijs(65, False, 10))  #ouderen doordeweeks (uitkomst is 5.6)
        print(ritprijs(11, True, 10))   #kinderen weeekend(uitkomst is 5.2 )
        print(ritprijs(12, True, 10))   #overig weekend (uitkomst is 4.8)
        print(ritprijs(64, True, 10))   #overig weekend (uitkomst is 4.8)
        print(ritprijs(65, True, 10))   #ouderen weekend(uitkomst is 5.2 )


        #positieve afstanden >50km
        print('positieve afstanden >50km:')
        print(ritprijs(64, False, 60))     #afstand groter dan 50km dus 15€+60*0.6 (uitkoms is 51)
        print(ritprijs(11, False, 60))     #afstand groter dan 50km voor kinderen(uitkomst is 35.7)
        print(ritprijs(12, False, 60))     #afstand groter dan 50km overig (uitkomst is 51)
        print(ritprijs(65, False, 60))     #afstand groter dan 50km voor ouderen(uitkomst is 35.7)
        print(ritprijs(11, True, 60))      #afstand groter dan 50km voor kinderen in het weekend(uitkomst is 33.15)
        print(ritprijs(12, True, 60))      #afstand groter dan 50km overig in het weekend overig (uitkomst is 30.6)
        print(ritprijs(64, True, 60))      #afstand groter dan 50km overig in het weekend(uitkomst is 30.6)
        print(ritprijs(65, True, 60))      #afstand groter dan 50km voor ouderen in het weekend (uitkomst is 33.15)


        #negatieve afstanden:
        print('negatieve afstanden: ')
        print(ritprijs(64, False, -10))   #negatieve afstand overig (uitkomst is 0)
        print(ritprijs(11, False, -10))   #negatieve afstand kinderen (uitkomst is 0)
        print(ritprijs(12, False, -10))   #negatieve afstand overig (uitkomst is 0 )
        print(ritprijs(65, False, -10))   #negatieve afstand ouderen(uitkomst is 0)
        print(ritprijs(11, True, -10))    #negatieve afstand kinderen in het weekend (uitkomst is 0)
        print(ritprijs(12, True, -10))    #negatieve afstand overig in het weekend(uitomst is0)
        print(ritprijs(64, True, -10))    #negatieve afstand overig in het weekend (uitkomst is 0)
        print(ritprijs(65, True, -10))    #negatieve afstand ouderen in heet weekend (uitkomst is 0)




    else:
        # dit is de input variant
        leeftijd = eval(input("geef je leftijd: "))
        input_weekendrit = input("is het een weekend rit(ja/nee): ")
        afstandKM = eval(input("wat is de afstand van de rit: "))

        if input_weekendrit == 'ja' or input_weekendrit == 'Ja':  # hier maak ik een boolean van de invoer van weeekend rit
            weekendrit = True
        elif input_weekendrit == 'nee' or input_weekendrit == 'Nee':
            weekendrit = False
        else:
            print("u heeft geen geldige waarde ingevuld bij weekendrit")

        print('de ingevoerde rit kost', ritprijs(leeftijd, weekendrit, afstandKM))

test()
