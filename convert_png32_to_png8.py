from PIL import Image

def convert(filename):
	im = Image.open(filename)
	im.load()
	alpha = im.split()[-1]
	im = im.convert('RGB').convert('P', palette = Image.ADAPTIVE, colors = 255)
	mask = Image.eval(alpha, lambda a: 255 if a <= 1 else 0)
	im.paste(0, mask)
	im.save(filename, transparency = 0, dpi=(400,400))
	
def convert_folder(path = '.'):
	import os, datetime
	debut = datetime.datetime.now()
	for dossier, sd, fichiers in os.walk(path):
		for fichier in fichiers:
			print 'traitement de {}'.format(fichier)
			if fichier.upper().find('.PNG') > 0:
				convert(os.path.join(dossier, fichier))
	print debut - datetime.datetime.now()

if __name__ == '__main__':
	convert_folder()
