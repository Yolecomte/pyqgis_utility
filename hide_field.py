layer = qgis.utils.iface.activeLayer()
fields = layer.pendingFields()
hfields = ['k_geom', 'credit', 'document', 'etat','id_origine','importance','mot_clef','a_obj','tx','ty','to','vta','h_tpn','hta','prot_depa','prot_depb','prot_depc','prot_depd', 'insee']
for field in fields:
    if field.name() in hfields:
        layer.setEditorWidgetV2(layer.fieldNameIndex(field.name()),'Hidden')