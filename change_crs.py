from qgis.core import QgsCoordinateReferenceSystem, QgsMapLayerRegistry
import qgis.core
def change_crs (epsg):
    '''Fonction permettant de changer le systeme de coordonnee des couches d'un projet QGIS, attention il ne s'agit pas de reprjeter les couches, simplement 
    leurs assigner un scr different dans le projet'''
    legend = qgis.utils.iface.legendInterface()
    exp_crs = QgsCoordinateReferenceSystem(epsg, QgsCoordinateReferenceSystem.EpsgCrsId)
    for layer in QgsMapLayerRegistry.instance().mapLayers().values():
        if legend.isLayerVisible(layer):
            print(layer)
            layer.setCrs(exp_crs)