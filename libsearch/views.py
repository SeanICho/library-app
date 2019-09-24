from django.views.generic import ListView
# from models import EventDetails
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from selenium import webdriver
import os
from datetime import datetime
import time as t
from bs4 import BeautifulSoup
import pandas as pd
import json

import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup

# class EventListView(ListView):
#     model = EventDetails
#
#     def home(request):
#         events = model.objects.all()
#         return render(request, 'home.html', {'events': events})

def scrape(url, **class):
    session = requests.Session()
    session.headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    # url_mppl =
    # url_dppl =
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content.encode("utf-8"), "html.parser")

    event_data = soup.find_all(class_=class['event_data'])

    year_today = datetime.now().year

    event_change_message = ['' if event.find(class_=class['event_change_message']") == None else event.find(class_=class['event_change_message']).get_text() for event in event_data]
    event_title = [event.find(class_=class["event_title"]).get_text() for event in event_data]
    event_location = [event.find(class_=class['event_location']).get_text() for event in event_data]
    event_time = [event.find(class_=class['event_time']).get_text() for event in event_data]
    event_group = [event.find(class_=class['event_group']).get_text() for event in event_data]
    event_type = [event.find(class_=class['event_type']).get_text() for event in event_data]
    event_descr = [event.find(class_=class['event_descr']).get_text() for event in event_data]
    event_register = [True if event.find(class_=class['event_register']) != None else False  for event in event_data]

    
nmdl_class = {
    'event_data': "eelistevent-data"
    'event_change_message': "eelist-changed-message"
    'event_title':"eelisttitle"
    'event_location':"eelocation"
    'event_time':"eelisttime"
    'event_group':"eelistgroup"
    'event_type':"eelisttags"
    'event_descr':"eelistdesc"
    'event_register':"eventRegButton"
}
scrape('https://nmdl.libnet.info/events?r=thismonth', nmdl_class)
