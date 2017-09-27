def inlezen_beginstation(stations):
    inlst = False
    while inlst == False:
        invoer = input("geef uw beginstation op: ") #vraagt het beginstation op
        if invoer in stations:
            inlst == True  #geeft aan dat het station gevonden is en beindigd de loop
            return invoer #geeft het beginstation als returnwaarde van de functie
        else:# geeft een foutmelding als het station niet in de lijst staat
            print("deze trein komt niet in {}".format(invoer))

def inlezen_eindstation(stations,beginstation):
    run = False
    while run == False:
        invoer = input("geef uw eindstation op: ")
        if invoer in stations: # controleert of het station in de lijst staat
            if stations.index(invoer) > stations.index(beginstation): #controleert of het station na het beginstation is
                return invoer
                run = True
            else:#geeft foutmelding als het station voor het beginstation is
                print('dit station is voor uw beginstation')
        else:#geeft een foutmelding als het station niet in de lijst staat
            print('deze trein komt niet in {}'.format(invoer))

def omroepen_reis(stations,beginstation,eindstation):
    I_beginstation = stations.index(beginstation)+1 #vraagt de index van het station op en telt hier 1 bij op zodat de nummers beginnen bij 1 ipv 0
    I_eindstation = stations.index(eindstation)+1 #vraagt de index van het station op en telt hier 1 bij op zodat de nummers beginnen bij 1 ipv 0
    afstand = I_eindstation-I_beginstation #berekent de afstand tussen beide stations
    prijs = afstand*5 #berekent de prijs van de rit

    print('het beginstation {} is het {}e station in het traject'.format(beginstation,I_beginstation))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation,I_eindstation))
    print('de afstand bedraagd {} station(s)'.format(afstand))
    print('de prijs van je kaartje is {} euro'.format(prijs))
    print()
    print('jij stapt in de trein in {}'.format(beginstation))
    i = I_beginstation
    while i < I_eindstation-1:#print alle stations tussen het begin en het eind station
        print('- {}'.format(stations[i]))
        i+=1
    print('je stapt uit in {} '.format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert','Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
print()
omroepen_reis(stations, beginstation, eindstation)
