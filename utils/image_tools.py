from PIL import Image
from io import BytesIO
import math

'''
Function that takes the image file as a string of it's location.  It uses PIL to
open as an image file and scales the image to fit with in a set size.  The size
is passed as a list of two int [width, height]. Returns a file-like object with
the new image in it to be used in inserting into the presentation.
'''
def fit_image(image, size):

    imgIO = BytesIO()
    
    with open (image, 'r+b') as f:
        with Image.open(f) as image:

            img_format = image.format
            img = image.copy()
            img.thumbnail((size[0],size[1], Image.LANCZOS))

            new_img = Image.new('RGBA', (size[0], size[1]), (255,255,255,0))

            img_positition = (
                int(math.ceil((size[0]-img.size[0]) / 2)),
                int(math.ceil((size[1]-img.size[1]) / 2))
            )

            new_img.paste(img, img_positition)
            new_img.format = img_format
            new_img.save(imgIO,'PNG')

            imgIO.seek(0)

            return imgIO
