layer_adr_pt =  QgsMapLayerRegistry.instance().mapLayersByName('adresse_pt_1')[0]
layer_adr_line = QgsMapLayerRegistry.instance().mapLayersByName('troncon_fusion')[0]

ids = []
for point in layer_adr_pt.getFeatures():
    geom = point.geometry()
    for rue in layer_adr_line.getFeatures(): 
        geom_rue = rue.geometry().buffer(1,5)
        if geom.intersects(geom_rue):
            ids.append(point.id())
layer_adr_pt.setSelectedFeatures(ids)
        