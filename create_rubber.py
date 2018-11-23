#coding : utf-8
"""
Author : YoLecomte

To use in QGIS python console
"""

from qgis.core import *
from qgis.gui import QgsRubberBand
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QColor

layer = iface.activeLayer()
rubber = QgsRubberBand(iface.mapCanvas(), True)
rubber.setColor(QColor(255,0,0))
rubber.setBrushStyle(Qt.Dense6Pattern)
rubber.setWidth(4)
for feat in layer.getFeatures():
    rubber.setToGeometry(feat.geometry().buffer(100,5), None)



    