def indexes(string,letter):
    i=0
    lst=[]
    for char in string:
        i +=1
        if char in letter:
            lst.append(i-1)
    return (lst)
print(indexes('hallo ik ben arno','a'))