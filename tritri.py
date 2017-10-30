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
    point0 = line.interpolate(line.length()/2)
    #start and end point of the perpendicular line 
    cosa, cosb = cosdir_azim(azimuth-90)
    point1 = QgsPoint(point0.asPoint().x()+(20*cosa), point0.asPoint().y()+(20*cosb))
    cosa, cosb = cosdir_azim(azimuth+90)
    point2 = QgsPoint(point0.asPoint().x()+(20*cosa), point0.asPoint().y()+(20*cosb))
    #perpendicular line with 20 meters of offset each side
    line2 = QgsGeometry().fromPolyline([point1,point2])
    
    new_feat = QgsFeature()
    new_feat.setGeometry(line2)
    memory_layer.addFeatures([new_feat])
    i+=1

QgsMapLayerRegistry.instance().addMapLayer(memory_layer)
    