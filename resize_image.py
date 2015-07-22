import PIL, sys
from PIL import Image
from sys import argv

inputfile = ''
basewidth = 800

script, inputfile, basewidth = argv

outputfile = 'Resized/' + inputfile
		
img = Image.open(inputfile)
wpercent = (int(basewidth) / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((int(basewidth), hsize), PIL.Image.ANTIALIAS)
img.save(outputfile)
