import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

path = "dataset/images/"

value_width = 5
value_height = 1
final_image = Image.new('RGB', (28*value_width, 28*value_height))


for j in range(value_height):
    for i in range(value_width):
        im = Image.open(os.path.join(path, f"image_{j*value_width + i+1}.bmp"))
        final_image.paste(im, (i * 28, j * 28))

final_image.save("saved.png")
