import subprocess
import os

input_folder = 'C:/Users/ylecomte/Desktop/Tmp/ECW/'
zoom = '16-21'
output_folder = 'C:/Users/ylecomte/Desktop/Tmp/ECW/PNG/'

for file in os.listdir(input_folder):
    if file.endswith('ecw'):
        print '[processing] : ',file
            # Tuilages
        #cmd = " ".join(['gdal2tiles','-s','EPSG:2154','-e','-z',zoom,input_folder+file,output_folder])
            # Reprojection de tifs
        #cmd =  " ".join(['gdalwarp','-overwrite','-s_srs', 'EPSG:27562','-t_srs', 'EPSG:2154', '-of', 'GTiff' , '"'+input_folder+file+'"','"'+output_folder+file[:-4] + '.tif'+'"'])
            #ECW --> PNG 32 bits
        #cmd = " ".join(['gdal_translate','-co','"WORLDFILE=YES"', '-co','"COMPRESS=LZW"','-of', 'PNG' , '"'+input_folder+file+'"','"'+output_folder+file[:-4] + '.png'+'"'])
            # TIF 24bits --> PNG 24 bits
        cmd = " ".join(['gdal_translate','-co','"WORLDFILE=YES"', '-co','"COMPRESS=LZW"','-of', 'PNG' , '"'+input_folder+file+'"','"'+output_folder+file[:-4] + '.png'+'"'])
        print cmd
        sp = subprocess.Popen(cmd, shell=True, executable='C:/Program Files/QGIS 2.18/OSGeo4W.bat')
        stdout, stderr = sp.communicate()
        print stdout, stderr
        