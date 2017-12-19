from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.networkanalysis import *

#building the graph**
vl = qgis.utils.iface.mapCanvas().currentLayer()
director = QgsLineVectorLayerDirector(vl, -1, '', '', '', 3)
properter = QgsDistanceArcProperter()
director.addProperter(properter)
crs = qgis.utils.iface.mapCanvas().mapRenderer().destinationCrs()
builder = QgsGraphBuilder(crs)

#coordinates of the Start point and endPoint** 
pStart = QgsPoint(793652.368428,2095608.58596)
pStop = QgsPoint(793772.710169,2095612.20415)
tiedPoints = director.makeGraph(builder, [pStart, pStop])
graph = builder.graph()

#Calculation of the shortest path**    
tStart = tiedPoints[0]
tStop = tiedPoints[1]

idStart = graph.findVertex(tStart)
idStop = graph.findVertex(tStop)

(tree, cost) = QgsGraphAnalyzer.dijkstra(graph, idStart, 0)

if tree[idStop] == -1:
  print "Path not found"
else:
  p = []
  curPos = idStop
  while curPos != idStart:
    pnt = graph.vertex(graph.arc(tree[curPos]).inVertex()).point()

    p.append(pnt)

    curPos = graph.arc(tree[curPos]).outVertex()

  p.append(tStart)

 #I build here a polyline based on the points in the p[] array
geom = QgsGeometry.fromPolyline(p)


 # I add here my result in a memory layer called cable and i want to do it for every feature i get after transforming the qgsrubberband object     

v_layer = None
for layer in QgsMapLayerRegistry.instance().mapLayers().values():
   if layer.name() == 'cable':
        v_layer = layer
if v_layer is None: 
    v_layer = QgsVectorLayer("LineString", "cable", "memory")
    v_layer.addAttribute(QgsField("id", QVariant.String))
    v_layer.addAttribute(QgsField("type", QVariant.String))
    QgsMapLayerRegistry.instance().addMapLayers([v_layer])

pr = v_layer.dataProvider()
v_layer.startEditing()


seg = QgsFeature()
seg.setGeometry(geom)
pr.addFeatures( [seg] )


v_layer.commitChanges()