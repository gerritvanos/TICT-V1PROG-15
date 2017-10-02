import csv

def invoer():
    with open('pe9_4.csv', 'w') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))
        while True:
            artnr = input('geef het artikelnr')
            if artnr == 'einde':
                break
            artc = input('geef de aartikelcode')
            naam = input('geef de naam')
            voorrraad = input('geef de voorraad')
            prijs = input('geef de prijs')
            writer.writerow((artnr,artc,naam,voorrraad,prijs))
            print()
    outfile.close()

def uitvoer():
    with open('pe9_4.csv', 'r') as infile:
        regels = csv.reader(infile, delimiter=';')
        hprijs = 0.0
        som =0
        voorraad = 834080
        lst = []
        lst1 = []
        count = 0
        for regel in regels:
            if count > 0:
                if regel != []:
                    if float(regel[4]) > hprijs:
                        hprijs = float(regel[4])
                        lst.clear
                        lst = regel
                    if int(regel[3]) < voorraad:
                        voorraad = int(regel[3])
                        lst1.clear
                        lst1 = regel
                    som = som + int(regel[3])
            count +=1
        print('het duurste artikel is {} en kost {}'.format(lst[2],lst[4]))
        print('er zijn slechts {} van het product {}'.format(lst1[3],lst1[0]))
        print('in totaal hebben wij {} producten in het magazijn'.format(som))


    infile.close()

uitvoer()
