def average():
    zin = input("geef een zin op: ")
    woorden = zin.split()
    lst = []
    for woord in woorden:
        lst.append(len(woord))
    gem = sum(lst) / len(lst)
    print(gem)

average()