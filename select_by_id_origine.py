
id_origine = '73322_2011_0018_01'

#t**********************************************************************************************
legend = iface.legendInterface()
for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if legend.isLayerVisible(layer):
        if layer.wkbType() != 100 :
            to_select = []
            fields = [field.name() for field in layer.pendingFields()]
            if 'id_origine' not in fields:
                pass
            else: 
                for feat in layer.getFeatures():
                    if feat['id_origine'] == id_origine:
                        to_select.append(feat.id())
        layer.setSelectedFeatures(to_select)
        print layer.name() + ' --> ' + str(layer.selectedFeatureCount()) + " objets ont l'origine " + str(id_origine)
        