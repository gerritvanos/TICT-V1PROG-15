lengte = eval(input("geef uw lengte: "))
gewicht = eval(input('geef uw gewicht: '))
bmi = gewicht/((lengte/100)**2)

if bmi < 18.5:
    print("ondergewicht")
elif bmi >=18.5 and bmi <= 25:
    print('normaal')
else:
    print('overgewicht')