# python 3
# Adds a logo.png to the lower right corner
# to all .png files in the workin directory

import os
from PIL import Image

SQUARE_FIT_SIZE = 500
LOGO_FILENAME = 'logo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
print("..." * 50)
# print((os.listdir()))

print("is this working")
for filename in os.listdir('.'):
    print("this is the list directory")
#    print(os.listdir('.'))
    if not (filename.endswith('.png') or filename.endswith('.PNG')) or filename == LOGO_FILENAME:
        print(filename)
        continue #skips non image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size
    print(width)
    print(height)

#    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
#
#        if width > height:
#            height = int((SQUARE_FIT_SIZE / width) * height)
#            width = SQUARE_FIT_SIZE
#        else:
#            width = int((SQUARE_FIT_SIZE / height) * width)
#            height = SQUARE_FIT_SIZE
#
#        print('Resizing %s...' % (filename))
#        im = im.resize((width, height))

    print('adding the logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(filename)
