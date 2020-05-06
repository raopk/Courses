"""
To add fruit images and their descriptions from the supplier on the fruit catalog web-server, 
create a new Python script that will automatically POST the fruit images and
 their respective description in JSON format.
1.name
2.weight (in lbs)
3.description
Example in txt
Apple
500 lbs
Apple is one of the most nutritious and healthiest fruits. It is very rich in an
tioxidants and dietary fiber. Moderate consumption can not only increase satiety
,but also help promote bowel movements. Apple also contains minerals such as calcium and magnesium, 
which can help prevent and delay bone loss and maintain bone health. It is good for young and old. 
####Assignment###
Currently, there are no products in the fruit catalog web-server. 
You can create a test fruit entry by entering the following into the content field:
     {    
          "name": "Test Fruit", 
          "weight": 100, 
          "description": "This is the description of my test fruit", 
          "image_name": "icon.sheet.png"
     }
After entering the above data into the content field click on the POST button. 
Now visit the main page of your website (by going to http://[linux-instance-external-IP]/), 
and the new test fruit you uploaded appears.
"""
#!/usr/bin/env python3
import requests
import os
import json
import locale
import sys
import operator

base_images = "supplier-data/images/"
save_direction = "supplier-data/images"

base_descriptions = "supplier-data/descriptions"

params = dict()
url = "http://35.222.11.128/fruits/"

for file in os.listdir(base_descriptions):
     numberline = 0
     response = requests.get(url)
     if not response.ok:
          raise Exception("GET failed with status code {}".format(response.status_code))
     print("File name : " + file)
     file_name = os.path.join(base_descriptions,file)
     if file.split(".")[-1] == "txt":
          try:
               with open(file_name, 'r') as read_file:
                    for read_line in read_file:
                         #print(read_line.strip())
                         if numberline == 0: params['name'] = read_line.strip()
                         if numberline == 1: params['weight'] = read_line.strip().split(" ")[0]
                         if numberline == 2: params['description'] = read_line.strip()
                         numberline += 1
                    params['image_name'] = file.split(".")[0]+".jpeg"
               print("Successful posting file " + file)
               print(params)
          except:
               print("Error to open file {} in path {}".format(file, file_name))
     else:
          print("This file {} is not text file".format(file))

     response = requests.post(url, data=params)
     response.request.url
     response.request.body 
