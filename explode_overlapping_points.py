#coding : utf-8

"""
Author = YoLecomte
Date = 21/11/2018

Explode points on a circle in the active layer if points have duplicated 
geometries (overlapping points)
RADIUS is the radius of the circle to place the new points on.
works on point layers (use iface.activeLayer() to get the layer)

!! works on place so make a backup of your data before running it... !!
"""

from collections import defaultdict
import math

# Radius to use to create the circle
RADIUS = 100

def move_points(layer, result):
    
    if not layer.isEditable():
        layer.startEditing()
        
    for cluster in result.items():

        nb_feat = len(cluster[1])+1

        feats = cluster[1].append(cluster[0])
        feats = [feat.id() for feat in cluster[1]]
        layer.setSelectedFeatures(feats)
        angle_to_add = 360.0/nb_feat
        angle = 0
        for feat in layer.selectedFeatures():
            angle_rad = math.radians(angle)
            old_geom = feat.geometry().asPoint()
            delta_x, delta_y = (RADIUS * math.cos(angle_rad), RADIUS * math.sin(angle_rad))
            new_geom = QgsGeometry.fromPoint(QgsPoint(old_geom.x() + delta_x, old_geom.y()+ delta_y))
            layer.dataProvider().changeGeometryValues({feat.id() : new_geom})
            angle += angle_to_add
            print new_geom.exportToWkt()
            print angle
        print '------------'
        

def explode_duplicate_points(layer):
    """
    Check for duplicate (geometry) points in the active layer
    Results are stored in result variable which is a defaultdict with a feature 
    as key and a list of duplicate features as value.
    """
    
    #check if the layer is a Point layer
    if layer.geometryType() != 0:
        print "The layer is not a point layer...." 
        return
    
    result = defaultdict(list)
    already_find = []
    for feat in layer.getFeatures():
        if feat.id() in already_find:
           pass
        else:
            for duplicate in layer.getFeatures():
                if duplicate.id() == feat.id():
                    pass
                else:
                    if feat.geometry().intersects(duplicate.geometry().boundingBox().buffer(0.1)):
                        result[feat].append(duplicate)
                        already_find.append(duplicate.id())

    move_points(layer, result)

layer = iface.activeLayer()
explode_duplicate_points(layer)

        