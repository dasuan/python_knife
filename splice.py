#!/usr/bin/python
# Filename : 
import os, sys
from PIL import Image


print 'LLLLLLLLLL'


# im = Image.open("lena.jpg")
# print im.format, im.size, im.mode
# print 'showing'
# im.show()


#convert
# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     if infile != outfile:
#         try:
#             Image.open(infile).save(outfile)
#         except IOError:
#             print "cannot convert", infile

# import os, sys
# import Image
# size = 128, 128
# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             im = Image.open(infile)
#             im.thumbnail(size)
#             im.save(outfile, "JPEG")
#         except IOError:
#             print "cannot create thumbnail for", infile

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


# for infile in range(1, len(sys.argv)):
#     outfile = os.path.splitext(infile)[0] + "_crop.jpg"
#     if infile != outfile:
#         try:
#             im = Image.open(infile)
#             box = (100, 100, 400, 400)
#             region = im.crop(box)
            
#             im2 = Image.new("RGB", region.size)
#             box2 = (0,0)
#             im2.paste(region, box2)
#             im2.save(outfile, "JPEG")	

#         except IOError:
#             print "cannot create thumbnail for", infile            

