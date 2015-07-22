import PIL, sys, os, glob
from PIL import Image
from sys import argv
from glob import glob

basewidth = 800

script, basewidth = argv
outputfile = ''

outputpath = os.getcwd() + '/Resized/'

os.makedirs(outputpath,exist_ok=True)

filetypes = glob('*.gif')
filetypes.extend(glob('*.png'))
filetypes.extend(glob('*.bmp'))
filetypes.extend(glob('*.jpg'))

for f in filetypes:
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
