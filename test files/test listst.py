lst = [1,2,3,4,5,6,7,8,9,10,11,12]
s = '5; 1998'
sp = s.split(';')
print(sp[0])
if sp[0] in lst:
    lst.remove(sp)
print(lst)