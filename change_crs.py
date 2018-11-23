#coding : utf-8
"""
Author : YoLecomte

To use in QGIS python console
Change crs for visible layer
"""

from qgis.core import QgsCoordinateReferenceSystem, QgsMapLayerRegistry
import qgis.core

def change_crs (epsg):

    legend = qgis.utils.iface.legendInterface()
    exp_crs = QgsCoordinateReferenceSystem(epsg, QgsCoordinateReferenceSystem.EpsgCrsId)
    
    for layer in QgsMapLayerRegistry.instance().mapLayers().values():
        if legend.isLayerVisible(layer):
            print(layer)
            layer.setCrs(exp_crs)