import psycopg2
import psycopg2.extras
import re

PREFIX_METIER = 'EP'

def get_occurences_from_db(classe, champ):
    try:
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % ('PRO4','SIG_GESTION','django','sig','5432'))
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    except(Exception, psycopg2.DataBaseError) as error:
        print error

    cur.execute("SELECT * from structure.vue_liste_occurrences where nom_table = '%s' and nom_champ = '%s'" % (classe, champ))

    return [row['libelle_long'] for row in cur]


for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if layer.name()[0:len(PREFIX_METIER)] == PREFIX_METIER:
        code_classe = re.search('(.+?)__', layer.name()).group(1)
        for field in layer.pendingFields():
            db_occurences = get_occurences_from_db(code_classe, field.name())
            if len(db_occurences)>0:
                layer_occurences = layer.uniqueValues(layer.fieldNameIndex(field.name()))
                for occurence in layer_occurences:
                    if occurence not in db_occurences:
                        print code_classe,field.name(), occurence