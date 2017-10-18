#-*- coding: UTF-8 -*-
def find_duplicate_geom(layer):
    layer = QgsMapLayerRegistry.instance().mapLayersByName(layer)[0]
    unique_geom = []
    duplicate = []
    for feat in layer.getFeatures():
        if feat.geometry().exportToWkt() not in unique_geom:
            unique_geom.append(feat.geometry().exportToWkt())
        else : 
            duplicate.append(feat.id())
    
    print layer.name()
    print 'total = ' + str(layer.featureCount()) + ' objets'
    print 'objets traités = ' + str(len(unique_geom) +len(duplicate))
    print 'objets uniques = ' + str(len(unique_geom)) + ' objets'
    print 'objets dupliqués = ' + str(len(duplicate)) + ' objets'
    print '**********************'
    layer.setSelectedFeatures(duplicate)

find_duplicate_geom(QgsMapLayerRegistry.instance().mapLayersByName('lg_adresse_travail_AMEN')[0].name())



