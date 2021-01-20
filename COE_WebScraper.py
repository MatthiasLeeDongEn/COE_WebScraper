from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
import datetime
import schedule
import time

d = datetime.datetime.now()
hour = d.strftime('%H')
minute = d.strftime('%M')
dayofweek = d.strftime("%a")
day = d.strftime("%d")
month = d.strftime("%m")
year = d.strftime("%y")
filename = str(dayofweek + " " + day + "-" + month + "-" + year)+ ".csv"

time_now = str(hour + ':' + minute)

url = "https://onemotoring.lta.gov.sg/content/onemotoring/home/buying/coe-open-bidding.html"

source = requests.get(url).text
soup = BeautifulSoup(source, features="html.parser")


def time_finder():
    d = datetime.datetime.now()
    hour = d.strftime('%H')
    minute = d.strftime('%M')
    time_now = str(hour + ':' + minute)
    return(time_now)

#create the excel file
csv_file = open(filename,'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['CAT A','','','','','CAT B'])
csv_writer.writerow(['PRICE','QUOTA','BIDS','TIME','','PRICE','QUOTA','BIDS','TIME'])

csv_file.close()

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def data_finder():
    source = requests.get(url).text
    soup = BeautifulSoup(source, features="html.parser")
    article = soup.find(class_="section coe_details")
    table = article.tbody
    table_rows = table.find_all('tr')
    return(table_rows)

def row_generator(n):
    row = table_rows[n]
    tdlist = row.find_all('td')
    textlist = [i.text for i in tdlist]
    cat = textlist[2:5]
    return(cat)

def update_function():
    global table_rows
    table_rows = data_finder()
    time_now = time_finder()

    cat_A = row_generator(1)
    cat_B = row_generator(2)

    cat_A.append(time_now)
    cat_A.append(' ')
    cat_A.extend(cat_B)
    cat_A.append(time_now)

    print(cat_A)

    append_list_as_row(filename, cat_A)

update_function()
schedule.every().day.at("12:00").do(update_function)
schedule.every().day.at("12:30").do(update_function)
schedule.every().day.at("13:00").do(update_function)
schedule.every().day.at("13:30").do(update_function)
schedule.every().day.at("14:00").do(update_function)
schedule.every().day.at("14:30").do(update_function)
schedule.every().day.at("15:00").do(update_function)
schedule.every().day.at("15:30").do(update_function)
schedule.every().day.at("15:45").do(update_function)
schedule.every().day.at("15:50").do(update_function)
schedule.every().day.at("15:51").do(update_function)
schedule.every().day.at("15:52").do(update_function)
schedule.every().day.at("15:53").do(update_function)
schedule.every().day.at("15:54").do(update_function)
schedule.every().day.at("15:55").do(update_function)
schedule.every().day.at("15:56").do(update_function)
schedule.every().day.at("15:57").do(update_function)
schedule.every().day.at("15:58").do(update_function)
schedule.every().day.at("15:59").do(update_function)
schedule.every().day.at("16:00").do(update_function)

while True:
    schedule.run_pending()
    time.sleep(1)

