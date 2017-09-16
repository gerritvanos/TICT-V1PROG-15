def new_password(oldpassword,newpassword):
    for teken in newpassword :
        if teken in '0123456789':
            goed = True
        else:
            goed = False
    if (newpassword != oldpassword and len(newpassword)>=6) and goed==True:
        return (True)
    else:
        return (False)
oud=input("geef je oude wachtwoord op: ")
nieuw=input("geef het nieuwe wachtwoord op: ")
print(new_password(oud,nieuw))


#zou goed moeten zijn
res = new_password('vakProg17','python17')
print(res)
# hetzelfde wachtwoord dus False
print(new_password('huprog17','huprog17'))
#te kort nieuw wachtwoord
print(new_password('vakProg17','Pro17'))