infile = open('example.txt')
linecount = 0
wordcount = 0
charactercount = 0
for char in infile:
    infile.read(1)
    charactercount += 1
    if (char == '.\n') or (char == ' '):
        wordcount += 1
        if char == '\n':
            linecount += 1

print('Het aantal karakters is ' + str(charactercount))
print('Het aantal woorden is ' + str(wordcount))
print('Het aantal regels is ' + str(linecount))

infile.close()