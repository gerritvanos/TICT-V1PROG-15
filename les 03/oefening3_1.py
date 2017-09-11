naam  = input("wat is je naam: ")
age = eval(input("hoe oud ben je: "))

if age<18:
    stemmen = "je mag niet stemmen"
else:
    stemmen = "je mag stemmen."

print(naam + ", " + stemmen)