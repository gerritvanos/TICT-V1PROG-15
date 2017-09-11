s = "Guido van Rossum heeft programmeertaal Python bedacht."
def klinker (letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return (True)


for letter in s:
    if klinker(letter) == True:
        print(letter)