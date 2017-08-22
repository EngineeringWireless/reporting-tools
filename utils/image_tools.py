from PIL import Image
import math

'''
Function that takes the image file as a string of it's location.  It uses PIL to
open as an image file and scales the image to fit with in a set size.  The size
is passed as a list of two int [width, height]
'''
def fit_image(image, size):

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
            return new_img
