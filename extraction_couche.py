import os
from qgis.core import QgsProject, QgsCoordinateReferenceSystem,QgsVectorFileWriter,QgsMapLayerRegistry
def extraction_couche(txt, crs):
	'''Extrait les couches contenant une partie de texte (exemple AEP) et les envoi vers un repertoire de ce nom
		L'argument crs permet une reprojection par le code EPSG''' 
	path_project = QgsProject.instance().readPath("./") + '/7_DATAQGIS/' + txt
	if os.path.exists(path_project):
		pass
	else:
		os.makedirs(path_project)
	exp_crs = QgsCoordinateReferenceSystem(crs, QgsCoordinateReferenceSystem.EpsgCrsId)
	print (path_project)
	for layer in QgsMapLayerRegistry.instance().mapLayers().values():
		print (layer.name())
		if layer.name().find(txt) != -1:
			QgsVectorFileWriter.writeAsVectorFormat(layer, path_project + '/' + layer.name(), "utf-8", exp_crs, "ESRI Shapefile")