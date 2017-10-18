layer  = iface.activeLayer()
layer.startEditing()

def split_multigeom(layer):
    '''clean the geometry of a layer on the fly to only have single geometry'''
    remove_list=[]
    for feat in layer.getFeatures():
        remove_list=[]
        geom = feat.geometry()
        geom = geom.simplify(0.2)
        if geom.isMultipart(): #get the multi geom
            remove_list.append(f.id()) #prepare for deleting
            new_feature = [] #prepare for recreating
            for part in geom.asGeometryCollection(): # split the multigeom
                part_geom = part.geometry()
                vertices = [v for v in part]
                if len(vertices) > 2 :
                    print vertices
                else:
                    temp_feature = QgsFeature(f)
                    temp_feature.setGeometry(part)
                    new_feature.append(temp_feature)
            
                layer.addFeatures(new_feature)
            else:
                pass
        
    if len(remove_list) > 0:
        for id in remove_list:
            print 'removing {} '.format(str(id))
            layer.deleteFeature(id)


def find_Point_0(feat):
    '''find the first vertex of a line and '''
    geom = feat.geometry()
    gpoint = geom.vertexAt(0) #as a QgsPoint
    return gpoint

    
def snap_line(feat):
    geom = feat.geometry()
    
    '''Make an arrow topological'''
    pass
    
def remove_arrows_end(feat):
    '''remove the line which represent the end of the arrow'''

def put_in_the_right_order(feat):
    '''check if the arrow is well oriented and if not reorient'''
    pass

split_multigeom(layer)