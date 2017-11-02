import math

#layer to work with
    #point representing geophone (x,y,z)
point_geophone = QgsMapLayerRegistry.instance().mapLayersByName('HAN04_GEOPHONES')[0]
    #point representing road of the truck
point_truck = QgsMapLayerRegistry.instance().mapLayersByName('HAN04_CAMIONS')[0]

# Defining Function to work with ******************************************************
def create_line_from_point(layer):
    '''create line truck from the set of points'''
    line = QgsVectorLayer("LineString?crs=epsg:29902", 'line_truck', 'memory')
    line.startEditing()
    points = []
    for feat in layer.getFeatures():
        points.append(feat.geometry().asPoint())
    new_feat = QgsFeature()
    new_feat.setGeometry(QgsGeometry().fromPolyline(points))
    line.addFeatures([new_feat])
    line.commitChanges()
    QgsMapLayerRegistry.instance().addMapLayer(line)
    return line

def create_orthogonale_lines(point_geophone, line_truck, length):
    '''Create Orthogonale lines and intersection point with line_truck'''
    # usefull function
    def cosdir_azim(azim):
       az = math.radians(azim)
       cosa = math.sin(az)
       cosb = math.cos(az)
       return cosa,cosb
    
    #initialize layer to store results
    memory_layer = QgsVectorLayer("LineString?crs=epsg:29902", 'Orthogonal_line', 'memory')
    memory_layer.startEditing()
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
        point1 = QgsPoint(point0.asPoint().x()+(length*cosa), point0.asPoint().y()+(length*cosb))
        cosa, cosb = cosdir_azim(azimuth+90)
        point2 = QgsPoint(point0.asPoint().x()+(length*cosa), point0.asPoint().y()+(length*cosb))
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

#perform the process
line_truck = create_line_from_point(point_truck)
create_orthogonale_lines(point_geophone, line_truck, 20)