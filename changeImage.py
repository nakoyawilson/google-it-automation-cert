#!/usr/bin/env python3
from PIL import Image
import os

directory = "~/supplier-data/images/"
images = os.listdir(directory)
new_size = (600,400)

for image in images:
    image_name, image_extension = os.path.splitext(image)
    converted_image = image_name + ".jpeg"
    if image != converted_image:
        try:
            with Image.open(os.path.join(directory, image)) as im:
                im.convert("RGB").resize(new_size).save(directory + converted_image)
        except OSError:
            print("Image conversion failed.", image)