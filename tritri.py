import math

def cosdir_azim(azim):
       az = math.radians(azim)
       cosa = math.sin(az)
       cosb = math.cos(az)
       return cosa,cosb

point_geophone = QgsMapLayerRegistry.instance().mapLayersByName('RT03')[0]


memory_layer = QgsVectorLayer("LineString?crs=epsg:29902", 'memory', 'memory')
memory_layer.startEditing()

iter = point_geophone.getFeatures()
iter2 = point_geophone.getFeatures()
iter2.next()
i = 0 
while i in range(point_geophone.featureCount()-1):
    feat= iter.next()
    feat2 = iter2.next()
    geom1 = feat.geometry().asPoint()
    geom2 = feat2.geometry().asPoint()
    #line between the two consecutive point and azimuth
    line = QgsGeometry().fromPolyline([geom1,geom2])
    azimuth = geom1.azimuth(geom2)
    #point between two successive point
    point1 = line.interpolate(line.length()/2)
    cosa, cosb = cosdir_azim(azimuth+90)
    point2 = QgsPoint(point1.asPoint().x()+(20*cosa), point1.asPoint().y()+(20*cosb))
    
    line2 = QgsGeometry().fromPolyline([point1.asPoint(),point2])
    
    new_feat = QgsFeature()
    new_feat.setGeometry(line2)
    memory_layer.addFeatures([new_feat])
    i+=1

QgsMapLayerRegistry.instance().addMapLayer(memory_layer)
    