#!/usr/bin/env python3
import requests

directory = "~/supplier-data/images/"
images = os.listdir(directory)
url = "http://localhost/upload"
with open(images) as opened:
    for image in images:
        response = requests.post(url, files={"file": opened})