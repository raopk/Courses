"""
Write a Python script
This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:
Iterate through each file in the folder
For each file:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image to a new folder in .jpeg format
Use a nano editor for this purpose. You can name the file however you'd like. And make sure to save the updated images in the folder: /opt/icons/
You'll use lots of methods from PIL to complete this exercise. 
You can refer to Pillow for detailed explanations and have a look at the tutorials to help you build the script and complete the task.
"""

#!/usr/bin/env python3
import os
from PIL import Image
#base = r'C:\Users\sataw\Desktop\Picture'
#save_direction = r"C:\Users\sataw\Desktop\Picture\convert_jpg\ "
base = '/home/student-04-8b8eae5c143c/images/'
save_direction = "/home/student-04-8b8eae5c143c/images/opt/icons/"
for path in os.listdir(base):
     try:
          with Image.open(os.path.join(base, path)) as image:
               cover = image.resize((128,128))
               cover_rgb = cover.convert('RGB')
               cover_rgb.save("/opt/icons/{}".format(path), "JPEG")  # save not used the /home/ direction
     except:
          pass

