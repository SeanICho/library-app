from selenium import webdriver
import os
from datetime import datetime
import time as t
from bs4 import BeautifulSoup
import pandas as pd
import json
#import requests

def scrape(url, clss):
    # session = requests.Session()
    # session.headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    chromedriver = "chromedriver.exe"  #chromedriver should be installed and env variable shuould be setup in advance
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    # driver.get('https://nmdl.libnet.info/events?r=nextmonth')
    t.sleep(5)
    content = driver.page_source
    driver.quit()

    # url_mppl =
    # url_dppl =
    # content = session.get(url, verify=False).content
    soup = BeautifulSoup(content.encode("utf-8"), "html.parser")

    event_data = soup.find_all(class_=clss['event_data'])

    year_today = datetime.now().year

    event_change_message = ['' if event.find(class_=clss['event_change_message']) == None else event.find(class_=clss['event_change_message']).get_text() for event in event_data]
    event_title = [event.find(class_=clss["event_title"]).get_text() for event in event_data]
    event_location = [event.find(class_=clss['event_location']).get_text() for event in event_data]
    event_time = [event.find(class_=clss['event_time']).get_text() for event in event_data]
    event_group = [event.find(class_=clss['event_group']).get_text() for event in event_data]
    event_type = [event.find(class_=clss['event_type']).get_text() for event in event_data]
    event_descr = [event.find(class_=clss['event_descr']).get_text() for event in event_data]
    event_register = [True if event.find(class_=clss['event_register']) != None else False  for event in event_data]


    lib = pd.DataFrame(
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

    lib.to_csv("{}_library.csv".format(url[8:12]))
    print("{}_library.csv file has been created!".format(url[8:12]))


# nmdl_class = {
#     'event_data': "eelistevent-data",
#     'event_change_message': "eelist-changed-message",
#     'event_title':"eelisttitle",
#     'event_location':"eelocation",
#     'event_time':"eelisttime",
#     'event_group':"eelistgroup",
#     'event_type':"eelisttags",
#     'event_descr':"eelistdesc",
#     'event_register':"eventRegButton",
# }
# scrape('https://nmdl.libnet.info/events?r=thismonth', nmdl_class)


# lib = lib.to_json()
# file = open("niles_maine_library.json", "w")
# json.dump(lib, file)
# print("json file has been created!")
#
# file.close()
