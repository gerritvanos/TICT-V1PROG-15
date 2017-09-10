list = [1,2,3,4,5,6,7,8,9]
#A
midden = len(list)/2 +0.5 -1
print(midden)
#B
print(list[int(midden)])
#C
list.sort()
list.reverse()
print(list)
#D
list.append(list.pop(0))
print(list)

