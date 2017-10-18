# -*- coding: utf-8 -*-

from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

'''Create an image from the scratch, which is zoomed on a specific object'''

ID_PAR = '7401360000B0250'

layer = QgsMapLayerRegistry.instance().mapLayersByName("Parcelle cadastre SIG")[0]
if layer.isValid():
    print 'Layer find'
else:
    print 'Oops, layer can''t be find...'
canvas = iface.mapCanvas()
for f in layer.getFeatures():
    if f['ID_PAR'] ==  ID_PAR:
        geom = f.geometry()
        bb = geom.buffer(100,5).boundingBox()
        iface.mapCanvas().setExtent(bb)
        iface.mapCanvas().refresh()
        rubber = QgsRubberBand(qgis.utils.iface.mapCanvas(), True)
        rubber.setColor(QColor(255,0,0))
        rubber.setBrushStyle(Qt.Dense6Pattern)
        rubber.setWidth(4)
        rubber.setToGeometry(geom,None)
        #rubber.show()
        
#composition item
composer = QgsComposition(iface.mapCanvas().mapRenderer())
composer.setPaperSize(200.00,120.00,1)
composer.setPrintAsRaster(True)
composer.setPrintResolution(300)
composer.setPlotStyle(QgsComposition.Print)
#map item
x , y = 0 , 0
w , h = 200,120
composeMap = QgsComposerMap(composer, x ,y, w, h)
composeMap.zoomToExtent(bb)
composer.addItem(composeMap)

#EXPORTING THE IMG
dpi = composer.printResolution()
dpmm = dpi / 25.4
width = int(dpmm * composer.paperWidth())
height = int(dpmm * composer.paperHeight())

# create output image and initialize it
image = QImage(QSize(width, height), QImage.Format_ARGB32)
image.setDotsPerMeterX(dpmm * 1000)
image.setDotsPerMeterY(dpmm * 1000)
image.fill(0)

# render the composition
imagePainter = QPainter(image)
sourceArea = QRectF(0, 0, composer.paperWidth(), composer.paperHeight())
targetArea = QRectF(0, 0, width, height)
composer.render(imagePainter, targetArea, sourceArea)
imagePainter.end()

image.save("C:/Users/ylecomte/Desktop/Tmp/IMG/out.png", "png")
