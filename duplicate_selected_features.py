
layer =  QgsMapLayerRegistry.instance().mapLayersByName('PLANCHES_A43')[0]
layer.startEditing()

for elem in layer.selectedFeatures():
    new_feat = QgsFeature()
    new_feat.setGeometry(elem.geometry())
    new_feat.setAttributes(elem.attributes())
    layer.addFeatures([new_feat])
    print new_feat