#!/usr/bin/env python3
from PIL import Image
import os, sys

original_directory = "/Users/nakoya/Documents/Python/google-it-automation-cert/images/"
new_directory = "/Users/nakoya/Documents/Python/google-it-automation-cert/opt/icons/"
images = os.listdir(original_directory)

for image in images:
    image_name, image_extension = os.path.splitext(image)
    converted_image = image_name + ".jpeg"
    if image != converted_image:
        try:
            with Image.open(os.path.join(original_directory, image)) as im:
                im.rotate(270).resize((128,128)).convert("RGB").save(os.path.join(new_directory, converted_image))
        except OSError:
            print("Image conversion failed.", image)