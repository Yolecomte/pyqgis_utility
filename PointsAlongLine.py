from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QVariant
from qgis.core import *
from qgis.core import (QgsFeature, QgsGeometry,
                   QgsVectorLayer, QgsMapLayerRegistry,
                   QgsField, QGis)
from qgis.gui import *
from qgis.utils import iface
import math

def pointsAlongLine(dist):
  try:
    inputlayer = QgsMapLayerRegistry.instance().mapLayersByName('ADR_ROUTE__LineString')[0]
    print ('route-layer found')
    epsg = inputlayer.crs().postgisSrid()
    uri = "Point?crs=epsg:" + str(epsg) + "&index=yes"
    memlayer = QgsVectorLayer(uri, 'itpoint', 'memory')
    prov = memlayer.dataProvider()
    prov.addAttributes([QgsField("NAMETEXT", QVariant.String)])
    NAMETEXT_idx = memlayer.fieldNameIndex("NAMETEXT")
    memlayer.startEditing()
    for f in inputlayer.getFeatures():
      value = f.attribute('nom_rue')
      print value
      length = f.geometry().length()
      for distance in range (0, (int(length)), dist):
        feat = QgsFeature()
        feat.setGeometry(f.geometry().interpolate(distance))
        feat.setAttributes([value])
        prov.addFeatures([feat])
    memlayer.commitChanges()
    memlayer.updateExtents()
    QgsMapLayerRegistry.instance().addMapLayer(memlayer)
  except IndexError:
    print ('route does not exist')

pointsAlongLine(100)

