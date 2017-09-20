def toon_aantal_kluizen_vrij(): #deze functie geeft weer hoeveel kluizen er nog beschikbaar zijn
    infile = open('kluizen.txt')
    lst = infile.readlines()
    aantalbezet = len(lst)
    over = 12 - aantalbezet
    infile.close()
    print("er zijn nog {} kluizen beschikbaar\n".format(over))

def nieuwe_kluis(): #maakt een nieuwe kluis aan
    infile = open('kluizen.txt', 'r')
    lst = [1,2,3,4,5,6,7,8,9,10,11,12]
    kluizen = infile.readlines()
    for kluis in kluizen:
        info = kluis.split(';')
        kluisnr = int(info[0])
        if kluisnr in lst:
            lst.remove(kluisnr) #haalt de kluisnummers die in de text file staan uit de lijst

    if len(lst) != 0: #controleert of er nog kluizen vrij zijn
        outfile = open('kluizen.txt', 'r+')
        outfile.read()
        code = input("geef een code op(min 4 tekens lang): ")
        if len(code) >= 4: # controleert of de code langer is dan 4
            outfile.write('{};{}\n'.format(lst[0],code))
            print('u heeft kluisnummer: {}\n'.format(lst[0]))
        else:
            print("u heeft een te korte code ingevoerd probeer het nogmaals\n")
        outfile.close()
    else: #als er geen kluizen vrij zijn geeft dit een melding
        print('er zijn geen kluizen meer beschikbaar\n')
    infile.close()

def kluis_openen(): #opent de kluis
    infile = open('kluizen.txt')
    input_kluisnr = eval(input("geef uw kluisnr op: "))
    input_code = input("geef uw code op: ")
    kluizen = infile.readlines()
    for kluis in kluizen:
        info = kluis.split(';')
        kluisnr = int(info[0])
        code = info[1].strip()
        if kluisnr == input_kluisnr and code == input_code: #controleert of de ingevoerde kluis gelijk is aan het bestand
            print('correcte combinatie u kunt uw kluis openen\n')
            correct = True
            break
        else:
            correct = False
    if correct == False:
        print("deze combinatie is niet bij ons bekend\n")
    infile.close()

def kluis_teruggeven(): #haalt een kluis uit het bestand
    infile = open('kluizen.txt',)
    input_kluisnr = eval(input("geef uw kluisnr op: "))
    input_code = input("geef uw code op: ")
    kluizen = infile.readlines()
    correct = False
    for kluis in kluizen:
        info = kluis.split(';')
        kluisnr = int(info[0])
        code = info[1].strip()
        if kluisnr == input_kluisnr and code == input_code: #controleerd of de code en nr. overeenkomen met het bestand
            print('correcte combinatie uw kluis is vrijgegeven\n')
            correct = True
    infile.close()

    if correct == True: # als de codes goed zijn schrijft onderstaande code alles naar het bestand behalve die lijn
        outfile = open('kluizen.txt','w')
        for kluis in kluizen:
            info = kluis.split(';')
            kluisnr = int(info[0])
            code = info[1].strip()
            if  kluisnr != input_kluisnr and code != input_code: #als de regel niet de ingevoerde info bevat wordt deze teruggeschreven
                outfile.write(kluis)
        outfile.close()
    else:
        print("deze combinatie is niet bij ons bekend\n")

doorgaan = 1
while doorgaan == 1: # zorgt ervoor dat het programma blijft draaien

    print(' 1: Ik wil weten hoeveel kluizen nog vrij zijn \n 2: Ik wil een nieuwe kluis\n 3: Ik wil even iets uit mijn kluis halen\n 4: Ik geef mijn kluis terug\n 5: Ik wil stoppen')
    menukeuze = input("Wat is uw keuze(1,2,3,4,5): ")

    if menukeuze not in '12345': # zorgt ervoor dat er alleen 1,2,3,4,5 ingevoerd kan worden echter kan er ook nog 12 of 345 ingevoerd worden
        print("u heeft geen geldige waarde ingevoerd\n")
    #onderstaande code laat de gebruiker kiezen
    else:
        menukeuze = int(menukeuze)
        if menukeuze == 1:
            toon_aantal_kluizen_vrij()
        elif menukeuze == 2:
            nieuwe_kluis()
        elif menukeuze == 3:
            kluis_openen()
        elif menukeuze == 4:
            kluis_teruggeven()
        elif menukeuze == 5:
            break # stopt het programma
        else: # als het geen 1,2,3,4 of 5 is maar bijvoorbeeld 123 wordt er ook een foutmelding gegeven
            print("u heeft geen geldige invoer ingegeven")