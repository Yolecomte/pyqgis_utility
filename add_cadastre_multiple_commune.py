list_communes = [
    ('73002','Aiguebelle'),
    ('73007','Aiton'),
    ('73019','Argentine'),
    ('73053','Bourgneuf'),
    ('73074','La Chapelle'),
    ('73083','Les Chavannes-en-Maurienne'),
    ('73109','Epierre'),
    ('73117','Fourneaux'),
    ('73119','Freney'),
    ('73135','Hermillon'),
    ('73157','Modane'),
    ('73168','Montgilbert'),
    ('73194','Orelle'),
    ('73203','Pontamafrey-Montpascal'),
    ('73220',"Saint-Alban-d'Hurtieres"),
    ('73223','Saint-Andre'),
    ('73224','Saint-Avre'),
    ('73231','Saint-Etienne de Cuines'),
    ('73237',"Saint-Georges d'Hurtieres"),
    ('73248','Saint-Jean de Maurienne'),
    ('73250','Saint-Julien-Montdenis'),
    ('73252','Saint-Leger'),
    ('73255','Sainte-Marie de Cuines'),
    ('73256',"Saint-Martin d'Arc"),
    ('73258','Saint-Martin de la Porte'),
    ('73261','Saint-Michel de Maurienne'),
    ('73272','Saint-Pierre de Belleville'),
    ('73278','Saint-Remy de Maurienne'),
    ('73320','Villargondran')]


for insee,nom in list_communes:
    url = "url=http://inspire.cadastre.gouv.fr/scpc/"+insee+".wms?contextualWMSLegend=0&crs=EPSG:2154&dpiMode=7&featureCount=10&format=image/png&layers=AMORCES_CAD&layers=LIEUDIT&layers=CP.CadastralParcel&layers=SUBFISCAL&layers=CLOTURE&layers=DETAIL_TOPO&layers=HYDRO&layers=VOIE_COMMUNICATION&layers=BU.Building&layers=BORNE_REPERE&styles=&styles=&styles=&styles=&styles=&styles=&styles=&styles=&styles=&styles=&maxHeight=1024&maxWidth=1280"
    layer = QgsRasterLayer(url, insee + ' - ' + nom, 'wms')
    print layer.isValid()
    QgsMapLayerRegistry.instance().addMapLayer(layer)