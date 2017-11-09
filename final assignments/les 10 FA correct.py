def processXML(filename):
    import xmltodict
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationsdict = processXML('stations.xml')
stations = stationsdict['Stations']

print('Dit zijn de codes en types van de 4 stations:')
for station in stations['Station']:
    print('{:5} - {}'.format(station['Code'],station['Type']))

print()

print('Dit zijn de stations met een of meer synoniemen: ')
for station in stations['Station']:
    if station['Synoniemen'] is not None:
        synoniemen = station['Synoniemen']
        print('{:5} - {}'.format(station['Code'],synoniemen))

print()

print('Dit is de lange naam van elk station:')
for station in stations['Station']:
    namen = station['Namen']
    print('{:5} - {}'.format(station['Code'], namen['Lang']))