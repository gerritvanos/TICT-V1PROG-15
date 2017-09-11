getallenrij = [2,4,6,8,10,9,7]
aantal3 = 0

for getal in getallenrij:
    if getal%3 == 0:
       aantal3 = aantal3 + 1
        #of aantal3 += 1

print("het daantal getallen deelbaar door 3 is: ",aantal3)