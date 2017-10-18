layer_to_update =  QgsMapLayerRegistry.instance().mapLayersByName('ADR_REPERE_ROUTE__Point')[0]
layer_to_join = QgsMapLayerRegistry.instance().mapLayersByName('ADR_ROUTE__LineString')[0]

print layer_to_update.name() + ' --> OK'
print layer_to_join.name() + ' --> OK'

field_to_update = layer_to_update.fieldNameIndex('comment')
field_to_join = layer_to_join.fieldNameIndex('nom_rue')

print str(field_to_update) + ' --> OK'
print str(field_to_join) + ' --> OK'

layer_to_update.startEditing()

for f_to_update in layer_to_update.getFeatures():
    geom_up = f_to_update.geometry()
    for f_to_join in layer_to_join.getFeatures():
        geom_join = f_to_join.geometry()
        if geom_up.buffer(0.1,5).intersects(geom_join):
            value = f_to_join.attribute('nom_rue')
            layer_to_update.changeAttributeValue(f_to_update.id(),field_to_update, str(value))

    