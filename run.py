#! /usr/bin/env python3

import os
import requests

directory_path = "/data/feedback/"
feedback_files = os.listdir(directory_path)
for file in feedback_files:
    feedback_dictionary = {}
    with open(os.path.join(directory_path, file)) as f:
        lines = f.read().splitlines()
        title, name, date, feedback = lines
        feedback_dictionary["title"] = title
        feedback_dictionary["name"] = name
        feedback_dictionary["date"] = date
        feedback_dictionary["feedback"] = feedback
    response = requests.post("http://<corpweb-external-IP>/feedback/", data=feedback_dictionary)
    response.raise_for_status()