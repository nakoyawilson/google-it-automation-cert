from PIL import Image
import os

orginal_directory = "/Users/nakoya/Documents/Python/google-it-automation-cert/images"
new_directory = "/Users/nakoya/Documents/Python/google-it-automation-cert/opt/icons/"
for image in original_directory:
    image_name, image_extension = os.path.splitext(image)
    converted_image = image_name + ".jpg"
    if image != converted_image:
        try:
            with Image.open(image) as im:
                im.rotate(270).resize((128,128)).save(new_directory + converted_image)
        except OSError:
            print("Cannot convert image.", image)
