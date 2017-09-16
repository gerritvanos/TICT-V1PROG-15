def swop(lst):
    if len(lst)>1 :
        lst[0],lst[1]=lst[1],lst[0]
        return (lst)
    else:
        return ("geef een geldige lijst op")

lijst = [1,2,3,4]
print(swop(lijst))