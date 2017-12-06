
layer =  QgsMapLayerRegistry.instance().mapLayersByName('PLANCHES_A43')[0]
layer.startEditing()

def getmax_value():
    '''find the max value of k_geom to
    increment it for new feature and ensure the consistence of PK'''
    values = []
    for elem in layer.getFeatures():
        values.append(elem['k_geom'])
    return max(values)


max_k_geom = getmax_value()
print max_k_geom

for elem in layer.selectedFeatures():
    max_k_geom += 1
    new_feat = QgsFeature()
    new_feat.setGeometry(elem.geometry())
    new_feat.setAttributes(elem.attributes())
    new_feat.setAttribute(0, max_k_geom)
    layer.addFeatures([new_feat])
    print new_feat