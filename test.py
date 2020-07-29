# Read READ ME.txt before running the script.

# import the required libraries
import csv
import time
# from urllib.parser
# import quote
import pandas as p
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from twilio.rest import Client

msg_list = []
phoneNumbers = p.read_csv("phoneNumbers.csv")

fields = ['phone']

sellerPhone = ['8016237631']



filename = "phoneNumbers.csv"
csvfile1 = csv.reader(filename)
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields 
    csvwriter.writerow(fields)  
  
    csvwriter.writerows(sellerPhone)  
        
    # writing the data rows 
    if (sellerPhone not in csvfile1):
        print(csvfile1.)
        print('hello')