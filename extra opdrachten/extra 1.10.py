lst = [ 159.55 , 160.00 , 205.95, 128.83, 175.49]

lst.append(160.00)
print(lst)
print(lst.count(160))
print(min(lst))
index = lst.index(min(lst))
print(index)
lst.pop(index)
print(lst)
lst.sort()
print(lst)