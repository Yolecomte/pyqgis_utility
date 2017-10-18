import csv

layer = QgsMapLayerRegistry.instance().mapLayersByName('lg_adresse_travail_AMEN')[0]
layer.startEditing()

csvfile =  open('C:/Users/ylecomte/Desktop/classeur1.csv', 'rb')
reader = csv.reader(csvfile, delimiter=';')
header = next(reader,None)
print header

for row in reader:
    for feat in layer.getFeatures():
        if ','.join([str(feat['numero']),str(feat['nom_rue'])]) == str(row[2]) :
            #print row[1], row[3]
            layer.changeAttributeValue(feat.id(),layer.fieldNameIndex('commentair'), row[3])

reader = None
print 'done'
