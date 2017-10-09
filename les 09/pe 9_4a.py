import csv

def invoer():
    with open('pe9_4.csv', 'w', newline='') as outfile:
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

invoer()
