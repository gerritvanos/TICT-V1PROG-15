def censor(filename):
    infile = open(filename)
    outfile = open('censor.txt', 'w')
    regels = infile.readlines()
    for regel in regels:
        woord = regel.split()
        if len(woord) == 4:
            outfile.write('xxxx')
        else:
            outfile.write(str(woord))

censor('4_32.txt')