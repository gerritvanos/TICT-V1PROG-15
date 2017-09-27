week ={'ma':'maandag','di':'dindag','wo':'woensdag','do':'donderdag','vr':'vrijdag'}

week['di']='dinsdag'

print(week)

week['za']='zaterdag'

print(week)

for afkorting in week.keys():
    print(afkorting)
for langenaam in week.values():
    print(langenaam)
for beide in week.items():
    print(beide)

for afkorting in week.keys():
    print(afkorting,week[afkorting])
for afkorting in week:
    print('afkorint: {},lange naam:{}'.format(afkorting,week[afkorting]))