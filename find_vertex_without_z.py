ligne = QgsMapLayerRegistry.instance().mapLayersByName('3D_cable_aerien')[0]

uri = "Point?crs=epsg:3945&index=yes"
memlayer = QgsVectorLayer(uri, 'itpoint', 'memory')
memlayer.startEditing()


count = 0
for feat in ligne.getFeatures():
    geomV2 = feat.geometry().geometry()
    for i in range(0,geomV2.numPoints(),1):
        if geomV2.zAt(i) == 0:
            X = geomV2.xAt(i)
            Y = geomV2.yAt(i)
            point = QgsPoint(X,Y)
            new_feat = QgsFeature()
            new_feat.setGeometry(QgsGeometry().fromPoint(point))
            memlayer.addFeatures([new_feat])

QgsMapLayerRegistry.instance().addMapLayer(memlayer)

print count