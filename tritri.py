import math

# usefull function
def cosdir_azim(azim):
       az = math.radians(azim)
       cosa = math.sin(az)
       cosb = math.cos(az)
       return cosa,cosb

#layer to work with
    #point representing geophone (x,y,z)
point_geophone = QgsMapLayerRegistry.instance().mapLayersByName('point_geophone')[0]
    #line representing road of the truck (polyline3D)
line_truck = QgsMapLayerRegistry.instance().mapLayersByName('line_truck')[0]

#new layer to create and fill
    #perpendicular line to project points 
memory_layer = QgsVectorLayer("LineString?crs=epsg:29902", 'Orthogonal_line', 'memory')
memory_layer.startEditing()
    # point to get on the line truck  
memory_layer_point = QgsVectorLayer("Point?crs=epsg:29902", 'Point_on_the_line_truck', 'memory')
memory_layer_point.startEditing()

#initialize iterators on the point geophone
iter = point_geophone.getFeatures()
iter2 = point_geophone.getFeatures()
iter2.next()
i = 0 
while i in range(point_geophone.featureCount()-1):
    feat= iter.next()
    feat2 = iter2.next()
    #two consecutive points to proceed
    geom1 = feat.geometry().asPoint()
    geom2 = feat2.geometry().asPoint()
    #line between the two consecutive point and azimuth
    line = QgsGeometry().fromPolyline([geom1,geom2])
    azimuth = geom1.azimuth(geom2)
    #point at the middle of the two successive points
    point0 = line.interpolate(line.length()/2)
    #start and end point of the perpendicular line (at 20 meters each side)
    cosa, cosb = cosdir_azim(azimuth-90)
    point1 = QgsPoint(point0.asPoint().x()+(20*cosa), point0.asPoint().y()+(20*cosb))
    cosa, cosb = cosdir_azim(azimuth+90)
    point2 = QgsPoint(point0.asPoint().x()+(20*cosa), point0.asPoint().y()+(20*cosb))
    #perpendicular line with 20 meters of offset each side
    line2 = QgsGeometry().fromPolyline([point1,point2])
    #adding the line to memory layer
    new_feat = QgsFeature()
    new_feat.setGeometry(line2)
    memory_layer.addFeatures([new_feat])
    # intersection with the line truck
    for elem in line_truck.getFeatures():
        if line2.intersects(elem.geometry()):
            point_truck = line2.intersection(elem.geometry()).asPoint()
            new_feat2 = QgsFeature()
            new_feat2.setGeometry(QgsGeometry().fromPoint(point_truck))
            memory_layer_point.addFeatures([new_feat2])
    i+=1

QgsMapLayerRegistry.instance().addMapLayer(memory_layer)
QgsMapLayerRegistry.instance().addMapLayer(memory_layer_point)