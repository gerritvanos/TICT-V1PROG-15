def stats(filename):
    infile = open(filename)
    # hieronder volgt het regel deel
    regels = infile.readlines()
    aantalregels = len(regels)
    print('line count: ',aantalregels)

    #hieronder volgt het woorden deel
    aantalwoorden=0
    for regel in regels:
        woorden = regel.split()
        aantalwoorden = aantalwoorden + len(woorden)
    print('word count:',aantalwoorden)

    #hieronder volgt het karakter deel
    karakters = 0
    for regel in regels:
        karakters = karakters + len(regel)
    print('character count:', karakters)

    infile.close()

stats("example.txt")