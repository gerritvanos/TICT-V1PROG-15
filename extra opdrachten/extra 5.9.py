getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
even =0
oneven =0
somoneven = 0
someven = 0
for getal in getallenrij:
    if getal%2 == 0:
        even+=1
        someven = someven+getal
    else:
        oneven+=1
        somoneven = somoneven+getal
print("het aantal even getallen is: ",even,"en de som bedraagd",someven)
print("het aantal oneven getallen is: ",oneven, "en som bedraagd",somoneven)