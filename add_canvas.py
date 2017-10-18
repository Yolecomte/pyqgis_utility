from qgis.gui import *
from PyQt4.QtGui import *

canvas = QgsMapCanvas()
layer = QgsRasterLayer(r'C:/Users/ylecomte/Desktop/Tmp/IMG/apercu.png', 'layer')
crs_L93 = QgsCoordinateReferenceSystem(2154, QgsCoordinateReferenceSystem.EpsgCrsId)
crs_WGS84 = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId) 
layer.setCrs(crs_L93)
vlayer = QgsVectorLayer(r'C:/Users/ylecomte/Desktop/Tmp/KML/Base_speleo.kml', 'Base_speleo', 'ogr')
vlayer.setCrs(crs_WGS84)
print layer.extent()
QgsMapLayerRegistry.instance().addMapLayer(layer,False)
QgsMapLayerRegistry.instance().addMapLayer(vlayer,False)
 
canvas.setExtent(layer.extent())
canvas.setLayerSet([QgsMapCanvasLayer(vlayer),QgsMapCanvasLayer(layer)])
canvas.setDestinationCrs(crs_L93)
canvas.setCrsTransformEnabled(True)
canvas.show()


