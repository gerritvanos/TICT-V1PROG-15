#A
infile = open("Voorbeel5_5.txt",'r')
print(infile.read())
infile.close()
#B
infile = open("Voorbeel5_5.txt", 'r')
alles = infile.read()
lijst = alles.split()
infile.close()
print(lijst)
#C
infile = open("Voorbeel5_5.txt", 'r')
lijst = infile.readlines()
infile.close()
print(lijst)