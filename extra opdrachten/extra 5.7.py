woord = 'zomaareenstring'
zoek = input("geef een letter: ")
inwoord = False
for letter in woord:
    if letter == zoek:
        print("de ingevoerde letter zit in het woord")
        inwoord == True
        quit()

if inwoord == False:
    print("De ingevoerde letter zit niet in het woord")