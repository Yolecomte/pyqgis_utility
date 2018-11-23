#coding : utf-8
"""
Author : YoLecomte

To use in QGIS python console
"""


def duplicate_counter(layer, field):
    counter = {}
    for feat in layer.getFeatures():
        if feat[field] in counter:
            counter[feat[field]] += 1 
        else:
            counter[feat[field]] = 1

    return counter
     
layer = iface.activeLayer()
result = duplicate_counter(layer,'x_r')
print result