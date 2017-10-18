#-*- coding: utf-8 -*-
from osgeo import gdal, osr

src_filename ='C:/Users/ylecomte/Desktop/TOPO_A43/PNG32/3d_10755_A43_Planche2_1000e_Nov2013_lamb3.png'
dst_filename = 'C:/Users/ylecomte/Desktop/TOPO_A43/TIF8/3d_10755_A43_Planche2_1000e_Nov2013_lamb3.tif'

# Opens source dataset
src_ds = gdal.Open(src_filename)
format = "GTiff"
driver = gdal.GetDriverByName(format)

# Open destination dataset
dst_ds = driver.CreateCopy(dst_filename, src_ds, 0)

# Specify raster location through geotransform array
# (uperleftx, scalex, skewx, uperlefty, skewy, scaley)
# Scale = size of one pixel in units of raster projection
# this example below assumes 100x100
gt = [966060.017007556, 0.06350305969287611130354462533195, 0.0579748079,6467687.29234516, 0.0579748079, -0.06350305969287611130354462533195]

# Set location
dst_ds.SetGeoTransform(gt)

# Get raster projection
epsg = 2154
srs = osr.SpatialReference()
srs.ImportFromEPSG(epsg)
dest_wkt = srs.ExportToWkt()

# Set projection
dst_ds.SetProjection(dest_wkt)

# Close files
dst_ds = None
src_ds = None

