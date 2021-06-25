#!/usr/bin/env python3

import os
import requests

directory_path = "~/supplier-data/descriptions/"
descriptions = os.listdir(directory_path)

for text_file in descriptions:
    if text_file.endswith(".txt"):
        file_name, file_extension = os.path.splitext(text_file)
        image_name = file_name + ".jpeg"
        description_dictionary = {}
        with open(os.path.join(directory_path, text_file)) as d:
            lines = d.read().splitlines()
            name, weight, description = lines
            weight_as_list = weight.split()
            weight = int(weight_as_list[0])
            description_dictionary["name"] = name
            description_dictionary["weight"] = weight
            description_dictionary["description"] = description
            description_dictionary["image_name"] = image_name
    response = requests.post("http://[linux-instance-external-IP]/fruits/", data=description_dictionary)
    response.raise_for_status()