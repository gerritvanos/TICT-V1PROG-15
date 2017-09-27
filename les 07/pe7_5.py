klassenlijst = {}
def namen(name):
    if name in klassenlijst.keys():
        klassenlijst[name] +=1
    else:
        klassenlijst[name] = 1
    return klassenlijst

invoer = ' '
while invoer != '':
    invoer = input('volgende naam: ')
    if invoer != '':
        klassenlijst = namen(invoer)

for student in klassenlijst:
    if klassenlijst[student] >1:
        print('er zijn {} studenten met de naam {}'.format(klassenlijst[student],student))
    else:
        print('er is {} student met de naam {}'.format(klassenlijst[student],student))