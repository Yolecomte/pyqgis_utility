import subprocess
import os

input_folder = 'C:/Users/ylecomte/Desktop/Tmp/Tif/'
zoom = '16-21'
output_folder = 'C:/Users/ylecomte/Desktop/Tmp/Tif/Compress'

for file in os.listdir(input_folder):
    if file.endswith('tif'):
        print '[processing] : ',file
        #cmd = " ".join(['gdal2tiles','-s','EPSG:2154','-e','-z',zoom,input_folder+file,output_folder])
        cmd =  " ".join(['gdal_translate','-co','"COMPRESS=LZW"', input_folder+file,output_folder+file])
        print cmd
        sp = subprocess.Popen(cmd, shell=True, executable='C:/Program Files/QGIS Essen/OSGeo4W.bat')
        stdout, stderr = sp.communicate()
        print stdout, stderr
        