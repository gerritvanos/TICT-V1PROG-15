def rps(p1,p2):
    if (p1 == 'R' and p2 =='S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R'):
        print(1)
    elif (p2 == 'R' and p1 == 'S') or (p2 == 'S' and p1 == 'P') or (p2 == 'P' and p1 == 'R'):
        print(2)
    elif p1==p2:
        print(0)

p1 = input('R,P,S')
p2 = input('R P S')

rps(p1,p2)