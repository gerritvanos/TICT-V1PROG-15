import fractions
F= eval(input('enter the temperature in degrees fahrenheit:'))
c= float(fractions.Fraction(5,9) *  (F-32) )
print(c)
print("the temperature in degrees celsius is:" , c)