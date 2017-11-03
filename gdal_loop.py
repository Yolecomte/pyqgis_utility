import subprocess
import os

input_folder = 'C:/Users/ylecomte/Desktop/Tmp/ECW/TIF/'
zoom = '16-21'
output_folder = 'C:/Users/ylecomte/Desktop/Tmp/ECW/PNG/'

for file in os.listdir(input_folder):
    if file.endswith('tif'):
        print '[processing] : ',file
        #cmd = " ".join(['gdal2tiles','-s','EPSG:2154','-e','-z',zoom,input_folder+file,output_folder])
        #cmd =  " ".join(['gdalwarp','-overwrite','-s_srs', 'EPSG:27562','-t_srs', 'EPSG:2154', '-of', 'GTiff' , '"'+input_folder+file+'"','"'+output_folder+file[:-4] + '.tif'+'"'])
        cmd = " ".join(['gdal_translate','-co','"WORLDFILE=YES"', '-co','"COMPRESS=LZW"','-of', 'PNG' , '"'+input_folder+file+'"','"'+output_folder+file[:-4] + '.tif'+'"'])
        print cmd
        sp = subprocess.Popen(cmd, shell=True, executable='C:/Program Files/QGIS 2.18/OSGeo4W.bat')
        stdout, stderr = sp.communicate()
        print stdout, stderr
        