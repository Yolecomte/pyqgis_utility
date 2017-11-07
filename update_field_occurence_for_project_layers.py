# -*- coding: utf-8 -*-

for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    for field in layer.pendingFields():
            if field.name() == 'etat':
                print layer.name()
                layer.startEditing()
                for feat in layer.getFeatures():
                    print feat['etat']
                    if  feat['etat'] == u'Déposé':
                        print 'occurence trouvé'
                        layer.changeAttributeValue(feat.id(),layer.fieldNameIndex('etat'), u'Démonté')
                    
#            else : 
#                print layer.name(), '--', 'Pas de champ "etat"'