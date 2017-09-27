def code(invoerstring):
    uitvoerstring = ''
    for letter in invoerstring:
        new = ord(letter) + 3
        newletter = chr(new)
        uitvoerstring = uitvoerstring + newletter
    return uitvoerstring

print(code('RutteAlkmaarDen Helder'))