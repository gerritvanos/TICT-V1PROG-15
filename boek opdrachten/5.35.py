def pixels(lst):
    som = 0
    for item in lst:
        for item2 in item:
            if item2 >0:
                som +=1
    return som

lst1 = [[0,156,0,0],[34,0,0,0],[23,123,0,34]]
lst2 = [[123,56,255],[34,0,0],[23,123,0],[3,0,0]]

print(pixels(lst1))
print(pixels(lst2))