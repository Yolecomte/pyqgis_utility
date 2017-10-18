#-*- coding: utf-8 -*-
import re
for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if layer.name() == 'vue_liste_occurrences':
        OccurencesId = layer.id()
        listeTableChamp = []
        for feature in layer.getFeatures():
            attrs = feature.attributes()
            value = attrs[2]+attrs[3]
            listeTableChamp.append(value)

for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if layer.name()[0:2] == 'EP':
        fields = layer.pendingFields()
        for field in fields:
            if field.name() in ['k_geom', 'n_existe_p', 'importance', 'tx','ty','to','hta','vta','document','mot_clef','h_tpn'] :
                layer.setEditorWidgetV2(layer.fieldNameIndex(field.name()),'Hidden')
            elif field.name() == 'etat':
                fieldIndex = layer.fieldNameIndex(field.name())
                filterExpression = '*nom_schema* = |Edigeo| and *nom_table* = |GEOM| and  *nom_champ* = |etat|'
                filterExpression =filterExpression.replace('*','"')
                filterExpression =filterExpression.replace('|',"'")
                layer.setEditorWidgetV2(fieldIndex,'ValueRelation')
                layer.setEditorWidgetV2Config(fieldIndex,{'Layer': OccurencesId, 'Key': 'libelle_long', 'Value': 'libelle_long','FilterExpression': filterExpression})
            elif field.name() == 'classe':
                fieldIndex = layer.fieldNameIndex(field.name())
                filterExpression = '*nom_schema* = |Edigeo| and *nom_table* = |GEOM| and *nom_champ* = |classe|'
                filterExpression =filterExpression.replace('*','"')
                filterExpression =filterExpression.replace('|',"'")
                layer.setEditorWidgetV2(fieldIndex,'ValueRelation')
                layer.setEditorWidgetV2Config(fieldIndex,{'Layer': OccurencesId, 'Key': 'libelle_long', 'Value': 'libelle_long','FilterExpression': filterExpression})
            else:
                print re.search('(.+?)__', layer.name()).group(1)+field.name()
                if re.search('(.+?)__', layer.name()).group(1)+field.name() in listeTableChamp:
                    fieldIndex = layer.fieldNameIndex(field.name())
                    filterExpression = '*nom_schema* = |eau| and *nom_table* = |'+re.search('(.+?)__', layer.name()).group(1)+'| and  *nom_champ* = |'+field.name()+'|'
                    filterExpression =filterExpression.replace('*','"')
                    filterExpression =filterExpression.replace('|',"'")
                    layer.setEditorWidgetV2(fieldIndex,'ValueRelation')
                    layer.setEditorWidgetV2Config(fieldIndex,{'Layer': OccurencesId, 'Key': 'libelle_long', 'Value': 'libelle_long','FilterExpression': filterExpression})