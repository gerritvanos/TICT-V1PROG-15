def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')
s = "abc"
lijst = ['a','b','c']
print(lijst)
wijzig(lijst)
print(lijst)
#print(s)
#wijzig(s)
#print(s)
#werkt niet met string die heeft de atributen clear en append niet
lijst1 = ['d','e','f']
print(lijst1)
wijzig(lijst1)
print(lijst1)