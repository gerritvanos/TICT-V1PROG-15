import datetime
import csv

bestand = 'inloggers.csv'
with open(bestand, 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter = ';')
    while  True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        vandaag = datetime.datetime.today()
        datum = vandaag.strftime("%a %d %b %Y")
        tijd = vandaag.strftime("%H %M")
        datumtijd = datum + ' at ' + tijd
        writer.writerow((datumtijd, voorl, naam, gbdatum, email))
        print()
outfile.close()