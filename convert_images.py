#!/usr/bin/env python3
from PIL import Image
import os

original_directory = "/home/student-01-af640c4e9338/images/"
new_directory = "/opt/icons/"
images = os.listdir(original_directory)

if not os.path.exists(new_directory):
    os.makedirs(new_directory)

for image in images:
    image_name, image_extension = os.path.splitext(image)
    converted_image = image_name + ".jpg"
    if image != converted_image:
        try:
            with Image.open(os.path.join(original_directory, image)) as im:
                im.rotate(270).resize((128,128)).convert("RGB").save(new_directory + converted_image)
        except OSError:
            print("Image conversion failed.", image)