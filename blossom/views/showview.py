from django.shortcuts import get_object_or_404
from django.views import generic
from django.shortcuts import render
from blossom.models.EventModel import ShowEvent
from blossom.models.LocationModel import Location
from blossom.models.ShowModel import Show

from blossom.tables.scheduletable import RoomSchedule

from django_tables2 import SingleTableView


def roomListView(request,show_id):
    context = []
    rooms = Location.objects.filter(show=show_id)
    i = 1
    for room in rooms:
        data = {}
        events = getRoomEventList(room)
        table = RoomSchedule(events,prefix=f"table_{i}")
        data['room'] = room.name
        data['table'] = table
        context.append(data)
    return render(request,'blossom/show.html',context={'data':context})

class EventDetail(generic.DetailView):
    model = ShowEvent
    template_name = 'blossom/eventdetail.html'
    context_object_name = 'event'

class RoomEventList(generic.ListView):
    template_name = "blossom/rooms.html"
    context_object_name = "rooms"
    model = Location

def getRoomEventList(eventroom:Location):
    roomEvents = ShowEvent.objects.filter(room=eventroom)
    return roomEvents