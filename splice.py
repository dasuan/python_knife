#!/usr/bin/python
# Filename : 
import os, sys
from PIL import Image

im2 = Image.new("RGB",(866,23720))
outfile = "a.png"
i=0
for infile in sys.argv[1:]:
    if infile != outfile:
        try:
            im = Image.open(infile)
            y = i * 593 
            box2 = (0,y)
            im2.paste(im, box2)
            i = i + 1
            print i,y
        except IOError:
            print "cannot create thumbnail for", infile

im2.save(outfile, "PNG", quality = 100) 


       

