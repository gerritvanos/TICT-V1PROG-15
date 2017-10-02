invoer = input('voer een string in: ')

for karakter in invoer:
    asc = ord(karakter)

    print('{:2}{:4}{:4x}{:10b}'.format(karakter,asc,asc,asc))