def vowels(zin):
    i=0
    for letter in zin:
        i +=1
        if letter in 'AEOUIaeoui' :
            print(i-1)

vowels('Hello world')