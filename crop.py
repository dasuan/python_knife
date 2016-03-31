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


for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_crop.png"
    if infile != outfile:
        try:
            im = Image.open(infile)
            #box = (1024, 244, 917, 63)
            box = (1368, 244, 2234, 837)
            region = im.crop(box)
            
            im2 = Image.new("RGB", region.size)
            box2 = (0,0)
            im2.paste(region, box2)
            im2.save(outfile, "PNG", quality = 100)	

        except IOError:
            print "cannot create thumbnail for", infile


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

