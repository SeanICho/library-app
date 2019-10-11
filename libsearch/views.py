from django.views.generic import ListView
# from models import EventDetails
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

import

# class EventListView(ListView):
#     model = EventDetails
#
#     def home(request):
#         events = model.objects.all()
#         return render(request, 'home.html', {'events': events})


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
