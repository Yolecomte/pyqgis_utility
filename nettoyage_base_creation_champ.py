#-*- coding: utf-8 -*-
from PyQt4.QtCore import * 

#recupere la couche active dans le projet QGIS
base = qgis.utils.iface.activeLayer()
print base.featureCount()

#initie les listes
list = []
index_c = [8,9,10,11,14,15,17,19] # liste des champs à traiter

    # creation des champs recepteurs
#recuperation du nombre d'occurence pour les champs: 8: accès, 9: historique, 10: description, 11: hydrologie, 14:profondeur, 15: géologie, 17: faune, 19: développement
for f in index_c :
    index = []
    for feature in base.getFeatures():
        attribute = feature.attributes()
        fr = attribute[f]
        if fr == NULL:
            pass
        else:
            compte = fr.encode('utf-8').count('}')
            index.append(compte)
    print f, max(index)
    list.append(max(index))
print list

#creation des champs granulaires
cod = 'latin-1'
list_champ = [u'accès'.encode(cod),u'historique'.encode(cod),u'description'.encode(cod),u'hydrologie'.encode(cod),u'profondeur'.encode(cod),u'géologie'.encode(cod),u'faune'.encode(cod),u'développement'.encode(cod)]
e = 0
for champ in list_champ :
        k = 0
        for i in range(0,list[e],1):
            base.dataProvider().addAttributes([QgsField(champ+str(k)+"_b", QVariant.String), QgsField(champ+str(k), QVariant.String)])
            base.updateFields()
            k += 1
        e+= 1


    
