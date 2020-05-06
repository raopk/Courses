"""
Working with supplier images
In this section, you will write a Python script named changeImage.py to process the supplier images. 
***
You will be using the PIL library to update all images 
within ~/supplier-data/images directory to the following specifications:
Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG
Open a nano editor by using the following command:
"""

#!/usr/bin/env python3
import os
from PIL import Image
#base = r'C:\Users\sataw\Desktop\Picture'
#save_direction = r"C:\Users\sataw\Desktop\Picture\convert_jpg\ "
base = "supplier-data/images"
save_direction = "supplier-data/images"
for path in os.listdir(base):
     try:
          with Image.open(os.path.join(base, path)) as image:
               cover = image.resize((600,400))
               cover_rgb = cover.convert('RGB')
               filename = path.split(".")
               cover_rgb.save("supplier-data/images/{}.jpeg".format(filename[0]), "JPEG")  # save not used the /home/ direction
     except:
          pass 
