invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lst = invoer.split('-') #splitst getallen op het streepje en zet deze in een lijst
lst = [int(i) for i in lst] #maakt van strings in de lijst intergers
lst.sort()
groot = max(lst)
klein = min(lst)
aantal = len(lst)
som = sum(lst)
gem = som/aantal

print("gesorteerde list van ints: {}".format(lst))
print('grootste getal: {} en kleinste getal: {}'.format(groot,klein))
print('Aantal getallen: {} en som van de getallen: {}'.format(aantal,som))
print('gemiddelde: {}'.format(gem))