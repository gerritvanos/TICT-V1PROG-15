infile = open('kaartnummers.txt', 'r')
lijst = infile.readlines()
infile.close()
for onderdeel in lijst:
    kaartinfo = onderdeel.split(',')
    print("{} heeft kaartnummer: {}".format(kaartinfo[1].strip(),kaartinfo[0]))