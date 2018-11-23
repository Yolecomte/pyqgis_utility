#coding : utf-8
"""
Author : YoLecomte

To use in QGIS python console
"""

line_layer  = QgsMapLayerRegistry.instance().mapLayersByName('line_truck')[0]
point = QgsMapLayerRegistry.instance().mapLayersByName('RT03')[0]
line_layer.startEditing()

for feat in line_layer.getFeatures(): 
    for i, elem in enumerate(point.getFeatures()): 
        #get the point lying on the vertex
        if str(feat.geometry().vertexAt(i).x())+str(feat.geometry().vertexAt(i).y()) == str(elem.geometry().asPoint().x())+str(elem.geometry().asPoint().y()):
            #feat.geometry().geometry is a QgsLineStringV2
            feat.geometry().geometry().setZAt(i, elem['field_4'])
    print feat.geometry().exportToWkt()
    line_layer.changeGeometry(feat.id(), feat.geometry())