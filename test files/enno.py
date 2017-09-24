def vowels(string):
    for i in range(0,len(string)):
        if string[i] in 'aeouiAEUOI':
            return (i)
invoer = input("geef string")
print(vowels(invoer))