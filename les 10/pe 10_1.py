import xmltodict

with open('artiekelen.xml') as infile:
    info = xmltodict.parse(infile.read())
    regels = info['artikelen']
    for artiekel in regels['artikel']:
        print(artiekel['naam'])