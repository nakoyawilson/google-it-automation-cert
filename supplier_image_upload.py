#!/usr/bin/env python3
import requests
import os

directory = "~/supplier-data/images/"
images = os.listdir(directory)
url = "~/upload/"

for image in images:
    if image.endswith(".jpeg"):
        try:
            with open(directory + image, 'rb') as opened:
                response = requests.post(url, files={"file": opened})
        except FileNotFoundError:
            print("Image failed to upload.", image)