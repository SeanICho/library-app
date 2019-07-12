from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
import pandas as pd
import json
#import requests

chromedriver = "C:/Users/ict7292/webdrivers/chromedriver.exe"  #chromedriver should be installed and env variable shuould be setup in advance
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('https://nmdl.libnet.info/events?r=thismonth')
time.sleep(5)
html = driver.page_source
driver.close()

soup = BeautifulSoup(html.encode("utf-8"), 'html.parser')

#print(soup.prettify())
event_data = soup.find_all(class_="eelistevent-data")

event_change_message = ['' if event.find(class_="eelist-changed-message") == None else event.find(class_="eelist-changed-message").get_text() for event in event_data]
event_title = [event.find(class_="eelisttitle").get_text() for event in event_data]
event_location = [event.find(class_="eelocation").get_text() for event in event_data]
event_time = [event.find(class_="eelisttime").get_text() for event in event_data]
event_group = [event.find(class_="eelistgroup").get_text() for event in event_data]
event_type = [event.find(class_="eelisttags").get_text() for event in event_data]
event_descr = [event.find(class_="eelistdesc").get_text() for event in event_data]
event_register = [True if event.find(class_="eventRegButton") != None else False  for event in event_data]

"""
print (event_change_message)
print (event_title)
print (event_location)
print (event_time)
print (event_group)
print (event_type)
print (event_descr)
"""
event_table = pd.DataFrame(
    {
        'event_change_message': event_change_message,
        'event_title': event_title,
        'event_location': event_location,
        'event_time': event_time,
        'event_group': event_group,
        'event_type': event_type,
        'event_descr': event_descr,
        'event_register': event_register
    }
)

#print(event_table)

event_table.to_csv("niles_maine_library.csv")
print("csv file has been created!")

"""
event_table = event_table.to_json()
file = open("niles_maine_library.json", "w")
json.dump(event_table, file)
print("json file has been created!")

file.close()
"""
