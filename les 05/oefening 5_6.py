infile = open('kaartnummers.txt', 'r')
outfile = open('oefening5_6.txt', 'w')
lijst = infile.readlines()
infile.close()
for onderdeel in lijst:
    kaartinfo = onderdeel.split(',')
    outfile.write("{} heeft kaartnummer: {}\n".format(kaartinfo[1].strip(),kaartinfo[0]))

outfile.close()