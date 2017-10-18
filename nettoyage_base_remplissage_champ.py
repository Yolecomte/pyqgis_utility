#-*- coding: utf-8 -*-
from PyQt4.QtCore import * 

#recupere la couche active dans le projet QGIS
base = qgis.utils.iface.activeLayer()
print base.featureCount()


index_c = [8,9,10,11,14,15,17,19] #liste des index des champs à traiter

#nettoyage des chaines de caractères, mise en place d'un separateur et decoupage des chaines
for value in index_c :
    for feature in base.getFeatures():
        attribute = feature.attributes()
        fr = attribute[value]
        if fr == NULL:
            pass
        else:
            fr = fr.replace('[','')
            fr = fr.replace(']','')
            fr = fr.replace('{','')
            fr = fr.replace('/','')
            fr = fr.replace('}, ','|')
            fr = fr.replace('}','')
            fr = fr.replace('":','|')
            fr = fr.replace('"','')
            frs = fr.split('|')
            frs.append(value)
            base.startEditing()
            # remplissage des champs granulaires par index de champ origine,!ATTENTION! index du champs recepteurs en dur!
            if frs[-1] == 8:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 21+k,elem )
                    k += 1
                    print 'Acces '+ ' Done!'
            if frs[-1] == 9:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 29+k,elem )
                    k += 1
                    print 'Historique ' + ' Done!'
            if frs[-1] == 10:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 37+k,elem )
                    k += 1
                    print 'Description ' + ' Done!'
            if frs[-1] == 11:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 43+k,elem )
                    k += 1
                print 'Hydrologie ' + ' Done!'
            if frs[-1] == 14:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 47+k,elem )
                    k += 1
                    print 'Profondeur ' + ' Done!'
            if frs[-1] == 15:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 51+k,elem )
                    k += 1
                    print 'Geologie ' + ' Done!'
            if frs[-1] == 17:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 55+k,elem )
                    k += 1
                    print 'Faune ' + ' Done!'
            if frs[-1] == 19:
                k=0
                for elem in frs[:-1]:
                    base.changeAttributeValue(feature.id(), 59+k,elem )
                    k += 1
                    print 'Devellopement ' + ' Done!'