import processing
from PyQt4.QtCore import QVariant

layer_line = 'ADR_ROUTE__LineString'
layer_point = 'ADR_REPERE_ROUTE__Point'
field_to_fill = 'a_obj'

#****************************************************************************************

'''fonction de remplissage du champ a_obj des ponctuels en fonction de la ligne a laquelle ils sont rattaches'''
for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if layer.name() == layer_line:
        tlayer_line = layer
        print 'ok ligne'
    if layer.name() == layer_point:
        tlayer_point = layer
        print 'ok point'
    
def calculate_azimuth(layerSource):
    '''explose les lignes sources en bi-point, ajoute un champ 'temp' et le remplis avec l'azimuth de la ligne'''
    #exploser les lignes en bi-point et recuperer le layer resultat
    layer = processing.runalg("qgis:explodelines", layerSource.source(), None)
    print layer
    layer = QgsVectorLayer(layer.get('OUTPUT'), layerSource.name()+'00','ogr')
    print layer
    layer.startEditing()
    #creer un champ temp pour y stocker l'azimuth et recuperer son id
    azimuth_field = QgsField('temp', QVariant.Int)
    exp = QgsExpression('(atan((xat(-1)-xat(0))/(yat(-1)-yat(0)))) * 180/3.14159 + (180 *(((yat(-1)-yat(0)) < 0) + (((xat(-1)-xat(0)) < 0 AND (yat(-1) - yat(0)) >0)*2)))')
    layer.dataProvider().addAttributes([azimuth_field])
    layer.commitChanges()
    layer.startEditing()
    idx_layer = layer.fieldNameIndex('temp')
    #calculer l'azimuth de chaque ligne et rempli le champ temp avec cette valeur
    for f in layer.getFeatures():
        xy = f.geometry().asPolyline()
        azimuth = int(xy[0].azimuth(xy[1]))
        print azimuth
        layer.changeAttributeValue(f.id(),idx_layer, azimuth)
    layer.commitChanges()
    QgsMapLayerRegistry.instance().addMapLayer(layer)
    return layer

def orientation(layer_point,layer_line):
    '''remplis l'attribut a_obj avec l'azimuth du champ 'temp' du layer_line calcule avec calculate_azimtuh pour les objets dont a_obj n'est pas renseigne'''
    layer_point.startEditing()
    index = QgsSpatialIndex()
    lines = [feature for feature in layer_line.getFeatures()]
    for l in lines:
        index.insertFeature(l)
    #selectionner les objets dont l'attribut a_obj n'est pas renseigne
    expr = QgsExpression(field_to_fill.replace("'",'"')+' is NULL')
    it = layer_point.getFeatures(QgsFeatureRequest( expr ))
    ids = [i.id() for i in it]
    layer_point.setSelectedFeatures(ids)
    points = [feature for feature in layer_point.selectedFeatures()]
    #recuperer l'azimuth de la ligne qui intersecte et remplir a_obj avec cette valeur 
    idx_a_obj = layer_point.fieldNameIndex(field_to_fill)
    max = layer_point.selectedFeatureCount()
    for elem in layer_point.selectedFeatures():
        for f in index.intersects(elem.geometry().boundingBox().buffer(0.1)):
            azimuth = lines[f].attributes()[layer_line.fieldNameIndex('temp')]
            layer_point.changeAttributeValue(elem.id(),idx_a_obj, azimuth)   
    layer_point.commitChanges()

flayer_line = calculate_azimuth(tlayer_line)
orientation(tlayer_point, flayer_line)
print 'youpi'