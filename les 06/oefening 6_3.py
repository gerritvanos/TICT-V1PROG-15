zin = input("geef een zin: ")
list = zin.split()
acro= ''
for woord in list:
    acro = acro + woord[0].capitalize()
print(acro)

