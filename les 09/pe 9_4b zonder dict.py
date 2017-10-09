import csv
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