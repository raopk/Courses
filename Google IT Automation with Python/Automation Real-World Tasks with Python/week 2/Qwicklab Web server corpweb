"""
The script should now follow the structure:
1.List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
2.You should now have a list that contains all of the feedback files from the path /data/feedback. 
Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
3.Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
4.Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.
Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
5.Save the run.py script file by pressing Ctrl-o, the Enter key, and Ctrl-x.
"""



#! /usr/bin/env python3
import os
import requests

path = "/data/feedback"
#path = r"C:\Users\sataw\Desktop\Text" Test in my computer
params = dict()
url = "http://35.226.196.2/feedback/"

for file in os.listdir(path):
     numberline = 0
     response = requests.get(url)
     if not response.ok:
          raise Exception("GET failed with status code {}".format(response.status_code))
     print("File name : " + file)
     file_name = os.path.join(path,file)
     with open(file_name, 'r') as read_file:
          for read_line in read_file:
               #print(read_line.strip())
               if numberline == 0: params['title'] = read_line.strip()
               if numberline == 1: params['name'] = read_line.strip()
               if numberline == 2: params['date'] = read_line.strip()
               if numberline == 3: params['feedback'] = read_line.strip()
               numberline += 1

          response = requests.post(url, data=params)
          response.request.url
          response.request.body

          print("Successful posting file " + file)
