lijst = [1,2,3,4,5,6,7,8,9]

indexm = len(lijst) // 2
print(indexm)
print(lijst[indexm])
lijst.sort()
lijst.reverse()
print(lijst)
lijst.append(lijst.pop(0))
print(lijst)