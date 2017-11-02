layer = iface.activeLayer()

def add_z_values_from_field(layer,fieldname):
    layer.startEditing()
    for feat in layer.getFeatures():
        print feat.geometry().exportToWkt()
        wkt = 'POINTZ (' + str(feat.geometry().asPoint().x()) + ' ' + str(feat.geometry().asPoint().y()) + ' ' + str(feat[fieldname]) + ')'
        geom = QgsGeometry().fromWkt(wkt)
        print geom.exportToWkt()
        layer.changeGeometry(feat.id(),geom)

add_z_values_from_field(layer, 'z')