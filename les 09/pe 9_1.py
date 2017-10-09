try:
    bedrag = 4356
    pers = input('geef aan hoeveel personen er zijn: ')
    pers = int(pers)
    if pers < 0:
        print('negatieve getallen zijn niet toegestaan')
    else:
        pp = bedrag/pers
        print('het kost {} per persoon'.format(pp))
except(ZeroDivisionError):
    print('Delen door nul kan niet')
except(ValueError):
    print('Gebruik cijfers voor het invoeren van het aantal')
except:
    print('onjuiste invoer')
