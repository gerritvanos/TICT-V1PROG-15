def partiton(lst):
    for name in lst:
        if name[0] in 'ABCDEFGHIJKLM':
            print(name)

namelist=['Elenor','Evelyn','Sammy','Owen','Gavin']

partiton(namelist)