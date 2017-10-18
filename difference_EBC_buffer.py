layer = iface.activeLayer()
tampon = QgsMapLayerRegistry.instance().mapLayersByName('Tampon')[0]
layer.startEditing()

for feat in layer.getFeatures():
    if feat['TYPEPSC'] == '01':
        print 'decoupe de : feat '+ str(feat.id())
        for elem in tampon.getFeatures():
            geom = feat.geometry().difference(elem.geometry())
            print geom.exportToWkt() 
        #feat.clearGeometry()
        layer.changeGeometry(feat.id(),geom)
    