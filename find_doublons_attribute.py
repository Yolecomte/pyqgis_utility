layer = iface.activeLayer()
#nom_champ = 'MOT_DIRECTEUR'

direct = []
for feat in layer.getFeatures():
    adr = feat['numero'] + ' ' + feat['nom_rue']
    if adr not in direct:
        direct.append(adr)
    else :
        print feat['numero'] + ' ' + feat['nom_rue']