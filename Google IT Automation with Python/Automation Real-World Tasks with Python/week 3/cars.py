"""
Sales summary
In this section, let's view the summary of last month's sales for all the models offered by the company. 
This data is in a JSON file named car_sales.json. Let's have a look at it.
To simplify the JSON structure, here is an example of one of the JSON objects among the list.
{
        "id": 47,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murciélago",
                "car_year": 2002
        },
        "price": "$13724.05",
        "total_sales": 149
}
Here id, car, price and total_sales are the field names (key).
The script cars.py already contains part of the work, but learners need to complete the task by writing the remaining pieces. The script already calculates the car model with the most revenue (price * total_sales) in the process_data method. Learners need to add the following:
Calculate the car model which had the most sales by completing the process_data method, and then appending a formatted string to the summary list in the below forma:
"The {car model} had the most sales: {total sales}"
Calculate the most popular car_year across all car make/models (in other words, find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year) by completing the process_data method, and append a formatted string to the summary list in the below format:
"The most popular year was {year} with {total sales in that year} sales."
The challenge
Here, you are going to update a script cars.py. You will be using the above JSON data to process information. A part of the script is already done for you, where it calculates the car model with the most revenue (price * total_sales). You should now fulfil the following objectives with the script:
Calculate the car model which had the most sales.
a. Call format_car method for the car model. 2. Calculate the most popular car_year across all car make/models
Hint: Find the total count of cars with the car_year equal to 2005, equal to 2006, etc.
and then figure out the most popular year.
Open the cars.py file using nano editor followed by granting editor permission:
sudo chmod 647 ~/scripts/cars.py
nano ~/scripts/cars.py
Generate PDF and send Email
Once the data is collected, you will also need to further update the script to generate a PDF report and automatically send it through email.
To generate a PDF:
Use the reports.generate() function within the main function.
The PDF should contain:
A summary paragraph which contains the most sales/most revenue/most popular year values worked out in the previous step.
Note: To add line breaks in the PDF, use: <br/> between the lines.
A table which contains all the information parsed from the JSON file, organised by id_number. 
The car details should be combined into one column in the form <car_make> <car_model> (<car_year>).
Note: You can use the cars_dict_to_table function for the above task.
To send the PDF through email:
Once the PDF is generated, you need to send the email, using the emails.generate() and emails.send() methods.
Use the following details to pass the parameters to emails.generate():
From: automation@example.com
To: <user>@example.com
Subject line: Sales summary for last month
E-mail Body: The same summary from the PDF, but using \n between the lines
Attachment: Attach the PDF path i.e. generated in the previous step
"""
#!/usr/bin/env python3
#1.Calculate the car model which had the most sales.
#2.Generate PDF and send Email
#Here id, car, price and total_sales are the field names (key).
import json
import os
import operator
import reports
import emails
def new_data(table):
     car_data = {}
     car_data_tables = [['ID', "Car", "Price", "Total Sales"]]
     with open(table) as json_file:
          json_data = json.load(json_file)
          for data in json_data:
               car_data['id'] = data['id']
               car_data['car'] = str(data['car']['car_make']) +" "+str(data['car']['car_model']) + " (" + str(data['car']['car_year']) + ")"
               car_data['price'] = data['price']
               car_data['total_sales'] = data['total_sales']
               #car_data['summary'] = float(data['price'][1:]) * float(data['total_sales'])
               new_list = [car_data['id'], car_data['car'], car_data['price'], car_data['total_sales']]
               car_data_tables.append(new_list)
     return car_data_tables

def most_revenue(table):
     #['ID', 'Car', 'Price', 'Total Sales', 'Summary']
     data_table = new_data(table)
     data_table = data_table[1:]
     for data in data_table:
          data.append(float(data[2][1:]) * float(data[3]))
     data_table.sort(key= lambda x : x[4], reverse=True)
     Car_name = data_table[0][1]
     Summary_revenue = data_table[0][4]
     return "The {} generated the most revenue: ${}".format(Car_name,Summary_revenue)

def most_sales(table):
     #1.Calculate the car model which had the most sales by completing the process_data method, 
     # and then appending a formatted string to the summary list in the below forma:
     # "The {car model} had the most sales: {total sales}"
     #['ID', 'Car', 'Price', 'Total Sales', 'Summary']
     data_table = new_data(table)
     data_table = data_table[1:]
     data_table.sort(key= lambda x : x[3], reverse=True)
     Car_name = data_table[0][1]
     total_sale = data_table[0][3]
     return "The {} had the most sales: {}".format(Car_name,total_sale)
     
def most_popular(table):
     #2.Calculate the most popular car_year across all car make/models (in other words, 
     # find the total count of cars with the car_year equal to 2005, equal to 2006, etc. 
     # and then figure out the most popular year)
     # "The most popular year was {year} with {total sales in that year} sales."
     detail = {}
     with open(table) as json_file:
          json_data = json.load(json_file)
          for data in json_data:
               year = data['car']['car_year']
               number_car_sale = data['total_sales']
               if year not in detail.keys():
                    detail[year] = number_car_sale
               else:
                    detail[year] += number_car_sale
          #print("Success export most_popular detail")
     detail = sorted(detail.items(), key=operator.itemgetter(1), reverse=True)
     #print(detail)
     year, total_sales = detail[0]
     return "The most popular year was {} with {} sales.".format(year,total_sales)
     

#table_name = 'E:\GitHub\Python_Google-IT-Coursera\Automatically Generate a PDF and send it by Email\car_sales.json'
table_name = 'car_sales.json'

table_data = new_data(table_name)
text_mail = most_revenue(table_name) + "\n"
text_mail += most_sales(table_name) + "\n"
text_mail += most_popular(table_name)

text_pdf = most_revenue(table_name) + "<br/>"
text_pdf += most_sales(table_name) + "<br/>"
text_pdf += most_popular(table_name)

#print(text_mail)


reports.generate("/tmp/cars.pdf", "Sales Summary for last month", text_mail, table_data)
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Sales summary for last month"
body = text_mail
message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
emails.send(message)
