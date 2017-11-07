layer_adr_line = QgsMapLayerRegistry.instance().mapLayersByName('lg_adresse_final')[0]
layer_adr_line.startEditing()
for feat in layer_adr_line.getFeatures():
    if feat.geometry().exportToWkt()[0:1] == 'M':
        geom = feat.geometry().asMultiPolyline()[0]
        Point1 = QgsPoint(geom[0])
        Point2 = QgsPoint(geom[1])
        print Point1,Point2
        geom_ = QgsGeometry.fromPolyline([Point1,Point2])
        print geom_
        layer_adr_line.changeGeometry(feat.id(),geom_)