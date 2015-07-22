import PIL, sys, os
from PIL import Image
from sys import argv

basewidth = 800

script, basewidth = argv
outputfile = ''

outputpath = os.getcwd() + '/Resized/'

os.makedirs(outputpath,exist_ok=True)

for f in os.listdir('.'):
    if os.path.isdir(f):
        # skip directories
        continue
	
    outputfile = 'Resized/' + f
    if os.path.isfile(outputfile):
        continue
    else:
	    img = Image.open(f)
	    wpercent = (int(basewidth) / float(img.size[0]))
	    hsize = int((float(img.size[1]) * float(wpercent)))
	    img = img.resize((int(basewidth), hsize), PIL.Image.ANTIALIAS)
	    img.save(outputfile)
