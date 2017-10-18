output_folder = 'C:/Users/ylecomte/Desktop/Tmp/QML/'

legend = iface.legendInterface()
for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if legend.isLayerVisible(layer):
        print layer.name()
        str1 = layer.source().find('vue_') + 4
        str2 = layer.source().find('(geom_') - 2
        code_classe = layer.source()[str1:str2]
        layer.saveNamedStyle(output_folder + code_classe + '.qml')
print 'QML generate in :' + output_folder
    