zin = input("geef een zin: ")

def gemiddelde(zin):
    woorden = zin.split()
    lst = []
    for woord in woorden:
        lst.append(len(woord))
    gem = sum(lst)/len(lst)
    return (gem)

print('de gemiddelde lengte van de woorden in deze zin is', gemiddelde(zin))