# -*- coding: utf-8 -*-

#~ Sert à gérer les occurrences pour les différents champs de la base.
#~ Placer le script dans le dosseir "plugin" de qgis
#~ dans la console, faire : import occurrences
#~ puis: occurrences.ajoute_occurences_pour_le_champ(cnig, champ)


from RechercheSigMajic.postgres import pg_connection
from RechercheSigMajic import postgres

def get_schema_table(cnig):
	sql = """SELECT "nom_schema", "nom_table"
			FROM "public"."table_cnig"
			WHERE "ID_CLASSE" = '%s';""" % cnig
	query = pg_connection.exec_(sql)
	query.next()
	record = query.record()
	nom_schema = record.value(0)
	nom_table = record.value(1)
	print nom_schema, nom_table
	return nom_schema, nom_table

def ajoute_occurences_pour_le_champ(cnig, champ):
	"""Ajoute les occurrences existantes dans la base pour le champ pour le code cnig concerné
	ATTENTION: On ne filtre pas encore les objets sur le code CNIG. On prend toutes les occurrences de ce champ, quel que soit le cnig de l'objet.
	A développer lorsque nous aurons l'applicatino qui gère le dictionnaire des données."""
	nom_schema, nom_table = get_schema_table(cnig)
	sql = u"""SELECT DISTINCT "%s"
			FROM "%s"."%s";""" % (champ, nom_schema, nom_table)
	print sql
	query = pg_connection.exec_(sql)
	valeurs = []
	while query.next():
		valeurs.append(query.record().value(0))
	print valeurs
	for valeur in valeurs:
		query = pg_connection.exec_("""INSERT INTO public.occurrence ("cnig", "nom_champ", "libelle_long")
		VALUES ('%s', '%s', '%s');""" % (cnig, champ, valeur))
		print valeur, u'ajoutée'
	pg_connection.commit()
		
def remplace_valeur(cnig, champ, ancienne, nouvelle):
	nom_schema, nom_table = get_schema_table(cnig)
	sql = u"""UPDATE "%s"."%s"
	SET "%s" = '%s'
	WHERE "%s" = '%s';""" % (nom_schema, nom_table, champ, nouvelle, champ, ancienne)
	print sql
	#~ query = pg_connection.exec_(sql)
	#~ pg_connection.commit()
	
def ajoute_occurence(cnig, champ, valeur):
	"""Ajoute une occurrence.
	ATTENTION: Bien mettre la valeur en unicode si elle contient des accents"""
	nom_schema, nom_table = get_schema_table(cnig)
	sql = u"""SELECT DISTINCT "%s"
			FROM "%s"."%s";""" % (champ, nom_schema, nom_table)
	print sql
	query = pg_connection.exec_(sql)
	query = pg_connection.exec_("""INSERT INTO public.occurrence ("cnig", "nom_champ", "libelle_long")
	VALUES ('%s', '%s', '%s');""" % (cnig, champ, valeur))
	print valeur, u'ajoutée'
	pg_connection.commit()
