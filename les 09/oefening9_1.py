try:
    numlist = [100, 101, 0, '103', 104]
    index = int(input('geef een index: '))
    print(100/numlist[index])
except(TypeError):
    print('u kunt niet delen door een string')
except(ValueError):
    print('u heeft geen geldige waarde ingevoerd(voer de index in als een integer)')
except(ZeroDivisionError):
    print('U kunt niet delen door nul(de list bevat een nul)')
except(IndexError):
    print('de lijst is zo groot niet')
