import os
from PIL import Image, ImageChops, ImageOps

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def process_images():
    if not os.path.exists('trimmed'):
        os.makedirs('trimmed')

    for filename in os.listdir('original'):
        if filename.endswith('.png'):
            im = Image.open(os.path.join('original', filename))
            im = trim(im)
            if im is not None:
                im.save(os.path.join('trimmed', filename))

process_images()