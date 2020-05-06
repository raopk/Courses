"""
1.Create a script reports.py to generate PDF report to supplier using the nano editor
Import all the necessary libraries(os, datetime and reports) that will be used to process the text data from the supplier-data/descriptions directory into the format below:
name: Apple
weight: 500 lbs
[blank line]
name: Avocado
weight: 200 lbs
[blank line]
2.Send report through email
Once the PDF is generated, you need to send the email using the emails.generate_email() and emails.send_email() methods.
Create emails.py using the nano editor using the following command:
     nano ~/emails.py
Define generate_email and send_email methods by importing necessary libraries.
Once you have finished editing the emails.py script, save the file by typing Ctrl-o, Enter key, and Ctrl-x.
Use the following details to pass the parameters to emails.generate_email():
     From: automation@example.com
     To: <user>@example.com
     Subject line: Upload Completed - Online Fruit Store
     E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
     Attachment: Attach the path to the file processed.pdf
Now, check the webmail by visiting [linux-instance-external-IP]/webmail. 
Here, you'll need a login to roundcube using the username and password mentioned in the Connection Details Panel on the left hand side,
followed by clicking Login.
Now you should be able to see your inbox, with one unread email. Open the mail by double clicking on it. 
There should be a report in PDF format attached to the mail. View the report by opening it.
"""

#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, additional_info, table_data):
     styles = getSampleStyleSheet()
     report = SimpleDocTemplate(filename)
     report_title = Paragraph(title, styles["h1"])
     report_info = Paragraph(additional_info, styles["BodyText"])
     table_style = [("GRID", (0,0), (-1,-1), 1, colors.black),
                    ('FONTNAME', (0,0), (-1, 0), "Helvetica-Bold"),
                    ('ALIGN', (0,0), (-1, -1), "CENTER")]
     empty_line = Spacer(1,20)
     if table_data != "": #Not data to create pdf file
          report_table = Table(data=table_data, style = table_style, hAlign="LEFT")
          report.build([report_title, empty_line, report_info, empty_line, report_table])
     else:
          report.build([report_title, empty_line, report_info, empty_line])
