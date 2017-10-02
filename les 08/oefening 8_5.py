import random

def dobbelworp(som):

    aantalgegooid = 0
    aantalgoed = 0
    while aantalgoed <100:
        steen1 = random.randrange(1, 7)
        steen2 = random.randrange(1, 7)
        if steen1+steen2 == som:
            aantalgoed += 1
        aantalgegooid += 1


    print('er is {} keer gegooid'.format(aantalgegooid))



in_som = eval(input("geef de som van 2 stenen: "))

dobbelworp(in_som)