import xmltodict

with open('stations.xml', 'r') as infile:
    info = xmltodict.parse(infile.read())
    stations = info['Stations']
    infile.close()

    print('Dit zijn de codes en types van de 4 stations:')
    for station in stations['Station']:
        print('{:5} - {}'.format(station['Code'],station['Type']))
    print()

    print('Dit zijn de stations met een of meer synoniemen: ')
    for staion in stations['Station']:
        print(station)
        if station['Synoniemen'] is not None:
            synoniemen = station['Synoniemen']
            print(synoniemen)

    print()
    print('Dit is de lange naam van elk station:')
    for station in stations['Station']:
        namen = station['Namen']
        print('{:5} - {}'.format(station['Code'],namen['Lang']))