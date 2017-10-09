import csv
def uitvoer():
    with open('pe9_4.csv', 'r') as infile:
        regels = csv.DictReader(infile, delimiter=';')
        hprijs = 0.0
        som =0
        voorraad = 834080
        dict = []
        dict1 = []
        for regel in regels:
            if float(regel['Prijs']) > hprijs:
                hprijs = float(regel['Prijs'])
                dict.clear
                dict = regel
            if int(regel['Voorraad']) < voorraad:
                voorraad = int(regel['Voorraad'])
                dict1.clear
                dict1 = regel
            som = som + int(regel['Voorraad'])
        print('het duurste artikel is {} en kost {}'.format(dict['Naam'],dict['Prijs']))
        print('er zijn slechts {} van het product {}'.format(dict1['Voorraad'],dict1['Artikelnummer']))
        print('in totaal hebben wij {} producten in het magazijn'.format(som))


    infile.close()

uitvoer()