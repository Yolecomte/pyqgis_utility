ligne = QgsMapLayerRegistry.instance().mapLayersByName('3D_cable_souterrain')[0]
point = QgsMapLayerRegistry.instance().mapLayersByName('gs')[0]

ligne.startEditing()

idx = QgsSpatialIndex()
allfeatures = {feature.id() : feature for (feature) in point.getFeatures()}
map(idx.insertFeature,allfeatures.values())

for elem in ligne.getFeatures():
    geom = elem.geometry().geometry()
    ids = idx.intersects(elem.geometry().boundingBox())
    for index in range(0,geom.numPoints(),1):
        geom_searcher = QgsGeometry.fromPoint(QgsPoint(geom.xAt(index),geom.yAt(index))).buffer(0.1,5)
        for id in ids:
            point = allfeatures[id]
            if geom_searcher.intersects(point.geometry()):
                geom.setZAt(index, float(point['ALT']))
    new_geom = geom.asWkt()
    print new_geom
    ligne.changeGeometry(elem.id(), QgsGeometry().fromWkt(new_geom))
                #print geom.xAt(index),geom.yAt(index), geom.zAt(index)
                #print point.geometry().geometry().z()

print 'finish'