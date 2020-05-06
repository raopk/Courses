"""
Health check
This is the last part of the lab, where you will have to write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. 
Moreover, this Python script should send an email if there are problems, such as:
     Report an error if CPU usage is over 80%
     Report an error if available disk space is lower than 20%
     Report an error if available memory is less than 500MB
     Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""
#!/usr/bin/env python3
import emails
import psutil
import os
import json
import locale
import sys
import operator
import reports
import shutil #Check Hdd
import socket
import smtplib

def Check_Error(current_cpu, current_disk_space, current_memory, local_host):
     """ Report an error if CPU usage is over 80% """
     if float(current_cpu) >= 80:
          # TODO: send the PDF report as an email attachment
          sender = "automation@example.com"
          receiver = "{}@example.com".format(os.environ.get('USER'))
          subject = "Error - CPU usage is over 80%"
          body = "Please check your system and resolve the isssue an soon as possible"
          message = emails.generate_email(sender, receiver, subject, body, "")
          emails.send(message)

     "Report an error if available disk space is lower than 20%"
     if float(current_disk_space) <= 0.20:
          # TODO: send the PDF report as an email attachment
          sender = "automation@example.com"
          receiver = "{}@example.com".format(os.environ.get('USER'))
          subject = "Error - available disk space is lower than 20%"
          body = "Please check your system and resolve the isssue an soon as possible"
          message = emails.generate_email(sender, receiver, subject, body, "")
          emails.send(message)

     "Report an error if available memory is less than 500MB"
     if float(current_memory) <= 0.5:
          # TODO: send the PDF report as an email attachment
          sender = "automation@example.com"
          receiver = "{}@example.com".format(os.environ.get('USER'))
          subject = "Error - available memory is less than 500MB"
          body = "Please check your system and resolve the isssue an soon as possible"
          message = emails.generate_email(sender, receiver, subject, body, "")
          emails.send(message)

     "Report an error if the hostname 'localhost' cannot be resolved to 127.0.0.1 "
     if str(local_host) != "127.0.0.1":
          # TODO: send the PDF report as an email attachment
          sender = "automation@example.com"
          receiver = "{}@example.com".format(os.environ.get('USER'))
          subject = "Error - the hostname 'localhost' cannot be resolved to 127.0.0.1"
          body = "Please check your system and resolve the isssue an soon as possible"
          message = emails.generate_email(sender, receiver, subject, body, "")
          emails.send(message)


def main(argv):
     # gives a single float value
     current_cpu = psutil.cpu_percent()
     # gives an object with many fields
     current_memory = psutil.virtual_memory()
     # you can convert that object to a dictionary 
     current_memory_dict = dict(psutil.virtual_memory()._asdict())
     total, used, free = shutil.disk_usage("/")
     free_hdd = free // (2**30) 
     total_hdd = total // (2**30)
     #Current Hdd
     current_free_hdd = free_hdd/total_hdd
     local_host = socket.gethostbyname(socket.gethostname())
     #print("Total: %d GiB" % (total // (2**30)))
     #print("Used: %d GiB" % (used // (2**30)))
     #print("Free: %d GiB" % (free // (2**30)))

     #print("Current Memory = " + str(current_memory))
     #print("Current Memory(dict) = " + str(current_memory_dict))
     current_memory_GB = current_memory_dict['available'] / (2**30) 

     print("Current CPU(%) = " + str(current_cpu))
     print("Current Disk_Space(%) = {0:.2f} (%) ".format(current_free_hdd))
     print("Current Memory(GB) = " + str(current_memory_GB))
     print("Current local_host : {}".format(local_host))

     #Check_Error(current_cpu, current_disk_space, current_memory, local_host)
     Check_Error(current_cpu, current_free_hdd, current_memory_GB, local_host)

if __name__ == "__main__":
     main(sys.argv)
