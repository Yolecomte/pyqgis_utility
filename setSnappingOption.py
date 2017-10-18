from PyQt4.QtGui import QDockWidget, QDialog,QComboBox
import csv

iface.mainWindow().findChild(QDockWidget, 'Snapping and Digitizing Options').findChild(QDialog).findChild(QComboBox,'mSnapModeComboBox').setCurrentIndex(2)

def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError

def snap_configuration(code_classe):
    dict = {}
    for layer in QgsMapLayerRegistry.instance().mapLayers().values():
        c_classe = layer.source()[layer.source().find('vue_') + 4:layer.source().find('(geom_') - 2]
        QgsProject.instance().setSnapSettingsForLayer(layer.id(), False,3,0,0,False)
        dict[c_classe] = layer.id()
    with open ('Z:/template/SNAP/snapConfig.csv', 'rb') as snapConfig:
        snap_csv = csv.reader(snapConfig, delimiter=';')
        next(snap_csv, None)
        cc_to_snap = [[row[1],row[2],row[3],row[4],row[5],row[6]] for row in snap_csv if row[0] == code_classe]
        for cc in cc_to_snap:
             QgsProject.instance().setSnapSettingsForLayer(dict[cc[0]], str_to_bool(cc[1]),int(cc[2]),int(cc[3]),float(cc[4]),str_to_bool(cc[5]))
             print cc

snap_configuration('EP_INCENDIE')
    
   