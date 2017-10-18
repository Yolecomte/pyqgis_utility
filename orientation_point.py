import processing
from PyQt4.QtCore import QVariant

layer_line = 'line'
layer_point = 'points'
field_to_fill = 'a_obj'
tolerance = 0.1
#****************************************************************************************

'''fonction de remplissage du champ a_obj des ponctuels en fonction de la ligne a laquelle ils sont rattaches'''
tlayer_line = QgsMapLayerRegistry.instance().mapLayersByName(layer_line)[0]
tlayer_point = QgsMapLayerRegistry.instance().mapLayersByName(layer_point)[0]
    
def calculate_azimuth(layerSource):
    '''explose les lignes sources en bi-point, ajoute un champ 'temp' et le remplis avec l'azimuth de la ligne'''
    #exploser les lignes en bi-point et recuperer le layer resultat
    layer = processing.runalg("qgis:explodelines", layerSource.source(), None)
    layer = QgsVectorLayer(layer.get('OUTPUT'), layerSource.name()+'00','ogr')
    layer.startEditing()
    #creer un champ temp pour y stocker l'azimuth et recuperer son id
    layer.dataProvider().addAttributes([QgsField('temp', QVariant.Int)])
    layer.commitChanges()
    layer.startEditing()
    #calculer l'azimuth de chaque ligne et rempli le champ temp avec cette valeur
    for f in layer.getFeatures():
        xy = f.geometry().asPolyline()
        azimuth = int(xy[0].azimuth(xy[1]))
        layer.changeAttributeValue(f.id(),layer.fieldNameIndex('temp'), azimuth)
    layer.commitChanges()
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
    #points = [feature for feature in layer_point.selectedFeatures()]    #recuperer l'azimuth de la ligne qui intersecte et remplir a_obj avec cette valeur 
    for elem in layer_point.selectedFeatures():
        for f in index.intersects(elem.geometry().boundingBox().buffer(tolerance)):
            azimuth = lines[f].attributes()[layer_line.fieldNameIndex('temp')]
            layer_point.changeAttributeValue(elem.id(),layer_point.fieldNameIndex(field_to_fill), azimuth)   
    layer_point.commitChanges()

flayer_line = calculate_azimuth(tlayer_line)
orientation(tlayer_point, flayer_line)