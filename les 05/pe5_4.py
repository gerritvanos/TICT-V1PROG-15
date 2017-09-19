import datetime
vandaag = datetime.datetime.today()
datum = vandaag.strftime("%a %d %b %Y")
tijd = vandaag.strftime("%H:%M:%S")
naam = input("geef de naam van de hardloper in : ")

outfile = open("hardlopers.txt", 'a')

outfile.write('{}, {}, {}\n'.format(datum,tijd,naam))
outfile.close()