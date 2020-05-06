#!/usr/bin/env python3
import os
import emails
import json
import locale
import sys
import operator
import reports
import os.path
import smtplib
import email.message

from datetime import date
today = date.today()
# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")

base_descriptions = "supplier-data/descriptions"
summary = []

#Datetime
from datetime import date
today = date.today()
# Textual month, day and year	
current_time = today.strftime("%B %d, %Y")

def main(argv):
     """Process the JSON data and generate a full report out of it."""
     for file in os.listdir(base_descriptions):
          file_name = os.path.join(base_descriptions,file)
          numberline = 0
          if file.split(".")[-1] == "txt":
               try:
                    with open(file_name, 'r') as read_file:
                         for read_line in read_file:
                              #Detail in PDF
                              if numberline == 0:
                                   summary.append("")
                                   summary.append("name: "+read_line.strip())
                              if numberline == 1: summary.append("weight: "+read_line.strip())
                              if numberline == 2: pass
                              numberline += 1
                    print("Successful open and keep data in file: " + file)
               except:
                    print("Error to open file {} in path {}".format(file, file_name))
          else:
               print("This file {} is not text file".format(file))

     #Summary is list data that post in the body pdf file
     print(summary)
     # TODO: turn this into a PDF report
     reports.generate_report(   "/tmp/processed.pdf", 
                         "Process Update on "+current_time,
                         "<br/>".join(summary),
                         "") #No table data

     # TODO: send the PDF report as an email attachment
     sender = "automation@example.com"
     receiver = "{}@example.com".format(os.environ.get('USER'))
     subject = "Upload Completed - Online Fruit Store"
     body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
     message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
     emails.send(message)

if __name__ == "__main__":
     main(sys.argv) 
