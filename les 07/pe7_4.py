def makedict(file):
    infile = open(file)
    ticker = {}
    regels = infile.readlines()
    infile.close()
    for regel in regels:
        info = regel.split(':')
        info[1]=info[1].strip()
        ticker[info[1]]=info[0]
    return (ticker)

ticker = makedict('tickersym.txt')

sym = input('enter ticker sym: ')
print('company name: {}'.format(ticker[sym]))


name = input('enter company name: ')
for sym in ticker:
    if ticker[sym] == name:
        print('ticker sym =',sym)