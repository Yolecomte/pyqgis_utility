#-*- coding: utf-8 -*-
'''script permettant de générer des fichiers .points compatible avec le géoreferenceur QGIS a partir d'un shape de point'''

import os

file = 'C:/Users/ylecomte/Desktop/TOPO_A43/7_DATAQGIS/point_insertion.shp'
layer = QgsVectorLayer(file, 'point_insertion', 'ogr')
name = [fichier[:-4] for fichier in os.listdir('C:/Users/ylecomte/Desktop/TOPO_A43/PNG8')]
for fich in name:
    txt = open('C:/Users/ylecomte/Desktop/TOPO_A43/points/'+fich+'.points', "w")
    txt.write('mapX,mapY,pixelX,pixelY,enable\n')
    print fich

for feature in layer.getFeatures():
    attribute = feature.attributes()
    origine = str(attribute[2])
    for fich in name:
        if fich == origine : 
            txt_a = open('C:/Users/ylecomte/Desktop/TOPO_A43/points/'+fich+'.points', "a")
            txt_a.write(str(attribute[0])+','+str(attribute[1])+','+str(attribute[4])+','+str(attribute[5])+',1'+'\n')