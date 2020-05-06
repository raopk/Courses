#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module


#Example
#url = "http://localhost/upload/"
#with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#    r = requests.post(url, files={'file': opened})

base = "supplier-data/images"
url = "http://35.222.11.128/upload/"
for path in os.listdir(base):
    try:
        with open('supplier-data/images/{}'.format(path), 'rb') as opened:
            print(path)
            if path.split(".")[-1] == "jpeg" or "jpg":
                r = requests.post(url, files={'file': opened})
                print("File {}.jpeg is succesful to upload".format(path))
    except:
        pass
