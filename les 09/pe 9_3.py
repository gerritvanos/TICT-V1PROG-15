import csv
lst = []
with open('pe9_3.csv', 'r') as myCSVFile:
    regels = csv.reader(myCSVFile, delimiter=';')
    hscore = 0
    for regel in regels:
        if int(regel[2]) > hscore:
            hscore = int(regel[2])
            lst.clear()
            lst = regel
print('de hoogste score is: {} op {} behaald door {}'.format(lst[2],lst[1],lst[0]))