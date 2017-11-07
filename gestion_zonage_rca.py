import os
from qgis.gui import *
from qgis.core import *
from PyQt4 import QtGui, QtCore

env_path = 'U:/Travocom718/Data/A43/A43_QGIS/07_DATAQGIS/'

list_commune = ['','73002','73007','73019','73053','73074','73083','73109','73117','73119','73135','73157','73168','73194','73203','73220','73223','73224','73231','73237','73248','73250','73252','73255','73256','73258','73261','73272', '73278','73320']

def load_zonage_rca(commune) :
    for com in commune :
        if os.path.exists(env_path + com + '/ZONAGE_RCA.shp'):
			layer = QgsVectorLayer(env_path + com + '/ZONAGE_RCA.shp','ZONAGE_RCA_'+ com, 'ogr')
			layer.loadNamedStyle('U:/Travocom718/Data/A43/A43_QGIS/10_RESSOURCES/QML/DPAC.qml')
			QgsMapLayerRegistry.instance().addMapLayer(layer)
			print com 
        else:
			print 'Pas de ZONAGE_RCA pour la commune ' + com
			
def save_zonage_rca(commune) :
    for com in commune:
        if os.path.exists(env_path + com + '/ZONAGE_RCA.shp'):
            version = max([int(file[12:13]) for file in os.listdir(env_path + com +  '/VERSIONS_ZONAGE_RCA')])
            layer = QgsVectorLayer(env_path + com + '/ZONAGE_RCA.shp','ZONAGE_RCA', 'ogr')
            QgsVectorFileWriter.writeAsVectorFormat(layer, env_path + com + '/VERSIONS_ZONAGE_RCA/' + 'ZONAGE_RCA_' + 'V' + str(version+1)+ '.shp', "utf_8", None, "ESRI Shapefile")
			

dial = QtGui.QDialog()
dial.setWindowTitle('Gestion Zonage RCA')
cb = QtGui.QComboBox()
loadRCA = QtGui.QPushButton()
loadRCA.setText('Load RCA')
saveRCA = QtGui.QPushButton()
saveRCA.setText('Save RCA')
cb.addItems(list_commune)
layout = QtGui.QGridLayout()
layout.addWidget(cb)
layout.addWidget(loadRCA)
layout.addWidget(saveRCA)
dial.setLayout(layout)
dial.show()

QtCore.QObject.connect(loadRCA, QtCore.SIGNAL("clicked ()"),lambda: load_zonage_rca([cb.currentText()]))




