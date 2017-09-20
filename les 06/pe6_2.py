list =  eval(input("Geef lijst met minimaal 10 strings: "))
def vierletterwoord(lst):
    if len(lst) >= 10:
        lst4 = []
        for s in lst:
            if len(s) == 4:
               lst4.append(s)
        return (lst4)
    else:
        print("u heeft minder dan 10 items ingevuld")

print('de nieuw-gemaakte lijst met alle vier-letter strings is:\n{}'.format(vierletterwoord(list)))