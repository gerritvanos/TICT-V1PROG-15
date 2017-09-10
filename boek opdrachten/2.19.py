awnsers =  ["Y", 'N', 'N', "Y", 'N', "Y", "Y", "Y", 'N', 'N', 'N']

numYes = awnsers.count("Y")
numNo = awnsers.count("N")
percentYes =  numYes/11 * 100

awnsers.sort()
f = awnsers.index("Y")

print(awnsers)
print(numYes)
print(numNo)
print(percentYes)
print(f)