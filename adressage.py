# -*- coding: utf-8 -*-

'''Connect two point layer with a line layer based on attribute'''

layer_adr_pt =  QgsMapLayerRegistry.instance().mapLayersByName('Adresse ponctuel')[0]
layer_adr_line = QgsMapLayerRegistry.instance().mapLayersByName('ADR_LIGNE_ADRESSE__LineString')[0]
layer_adr_rep_route = QgsMapLayerRegistry.instance().mapLayersByName('ADR_REPERE_ROUTE__Point')[0] 

layer_adr_line.startEditing()
prov = layer_adr_line.dataProvider()
for feat in layer_adr_pt.getFeatures():
    geom_adr = feat.geometry().asMultiPoint()[0]
    attr = feat['ADRPOST1']+'_'+feat['ADR_NUM']
    if attr == NULL:
        pass
    else:
        geom_route = [f.geometry().asPoint() for f in layer_adr_rep_route.getFeatures() if f['cnig']+'_'+f['nom'] == attr]
        geom_route = geom_route[0]
        geom_line = QgsGeometry.fromPolyline([geom_adr,geom_route])
        print geom_line
        new_feat = QgsFeature()
        new_feat.setGeometry(geom_line)
        prov.addFeatures([new_feat])

