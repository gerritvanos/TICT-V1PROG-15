bruin = ['boxtel','best','beukenlaan',"helmond 't houd", 'helmond', 'helmond brouwhuis', 'deurne']
groen = ['boxtel','best','beukenlaan','geldrop','heeze','weert']
bruinset=set(bruin)
groenset = set(groen)

print('deze stations zitten in beide trajecten{}'.format(bruinset.intersection(groenset)))
print('deze stations komen wel voor in bruin en niet in groen',bruinset.difference(groenset))
print('alle stations zijn',set(groen+bruin))