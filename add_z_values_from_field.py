#coding : utf-8
"""
Author : YoLecomte

To use in QGIS python console
"""

layer = iface.activeLayer()
layer.startEditing()
for feat in layer.getFeatures():
    print feat.geometry().exportToWkt()
    wkt = 'POINTZ (' + str(feat.geometry().asPoint().x()) + ' ' + str(feat.geometry().asPoint().y()) + ' ' + str(feat['field_4']) + ')'
    geom = QgsGeometry().fromWkt(wkt)
    print geom.exportToWkt()
    layer.changeGeometry(feat.id(),geom)