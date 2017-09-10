cijferICOR = 7.0
cijferCSN = 8.0
cijferPROG = 8.0

gemiddelde = (cijferCSN + cijferICOR + cijferPROG)/3
beloning = (cijferPROG + cijferICOR + cijferCSN) * 30
overzicht = 'mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning op van €' + str(beloning) + ' op!'

print(overzicht)