from qgis.core import *
from qgis.gui import *
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

layer = qgis.utils.iface.activeLayer()
rubber = QgsRubberBand(qgis.utils.iface.mapCanvas(), True)
rubber.setColor(QColor(255,0,0))
rubber.setBrushStyle(Qt.Dense6Pattern)
rubber.setWidth(4)
for feat in layer.getFeatures():
    rubber.setToGeometry(feat.geometry().buffer(100,5), None)



    