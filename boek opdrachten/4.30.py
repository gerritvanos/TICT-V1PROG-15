def distribution(filename):
    infile = open(filename)
    all = infile.read()
    list = all.split()
    countA = list.count('A')
    countA_ = list.count('A-')
    countB = list.count('B')
    countB_ = list.count('B-')
    countBplus = list.count('B+')
    countC = list.count('C')
    countC_ = list.count('C-')
    countF = list.count('F')

    print('{} students got A'.format(countA))
    print('{} students got A-'.format(countA_))
    print('{} students got B+'.format(countBplus))
    print('{} students got B'.format(countB))
    print('{} students got B-'.format(countB_))
    print('{} students got C'.format(countC))
    print('{} students got C-'.format(countC_))
    print('{} students got F'.format(countF))
distribution('4_30.txt')
