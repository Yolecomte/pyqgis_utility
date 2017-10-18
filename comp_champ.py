# -*- coding: utf-8 -*-

'''Comparaison of the field of two layer'''

for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if layer.name() == 'Reseau EP.shp':
       cable = layer
       print 'layer cable trouve'
    if layer.name() == 'OUVRAGE':
        ouvrage = layer
        print 'layer ouvrage trouve'

list_cable = [field.name() for field in cable.pendingFields()]
list_ouvrage = [field.name() for field in ouvrage.pendingFields()]
k = 0
while k < 643 :
    if list_cable[k] == list_ouvrage[k]:
        print list_cable[k],'  ||  ', list_ouvrage[k]
    k += 1
    