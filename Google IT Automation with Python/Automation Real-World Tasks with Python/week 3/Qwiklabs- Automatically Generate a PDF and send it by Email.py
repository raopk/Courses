  
#reports.py
#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info, table_data):
     styles = getSampleStyleSheet()
     report = SimpleDocTemplate(filename)
     report_title = Paragraph(title, styles["h1"])
     report_info = Paragraph(additional_info, styles["BodyText"])
     table_style = [("GRID", (0,0), (-1,-1), 1, colors.black),
                    ('FONTNAME', (0,0), (-1, 0), "Helvetica-Bold"),
                    ('ALIGN', (0,0), (-1, -1), "CENTER")]
     report_table = Table(data=table_data, style = table_style, hAlign="LEFT")
     empty_line = Spacer(1,20)
     report.build([report_title, empty_line, report_info, empty_line, report_table])

#email.py
#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
     """Create an email with an attachment. """
     #Basic Email formatting

     message = email.message.EmailMessage()
     message["From"] = sender
     message["To"] = recipient
     message["Subject"] = subject
     message.set_content(body)

     #Process the attachment and add it to the email
     attachment_filename = os.path.basename(attachment_path)
     mime_type, _ = mime_type.guess_type(attachment_path)          
     mime_type, mime_subtype = mime_type.split('/', 1)

     with open(attachment_path, 'rb') as ap:
          message.add_attachment(  ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)
     return message

def send(message):
     """Send the message to the configured SMTP server."""
     mail_server = smtplib.SMTP('localhost')
     mail_server.send_message(message)
     mail_server.quit()

#example.py
#!/usr/bin/env python3
import emails
import os
import reports
table_data=[
     ['Name', 'Amount', 'Value'],
     ['elderberries', 10, 0.45],
     ['figs', 5, 3],
     ['apples', 4, 2.75],
     ['durians', 1, 25],
     ['bananas', 5, 1.99],
     ['cherries', 23, 5.80],
     ['grapes', 13, 2.48],
     ['kiwi', 4, 0.49]]
reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."
message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
emails.send(message)
