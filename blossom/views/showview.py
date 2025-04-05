from django.shortcuts import get_object_or_404
from django.views import generic

from blossom.models.EventModel import ShowEvent
from blossom.models.LocationModel import Location
from blossom.models.ShowModel import Show


class ShowEvents(generic.ListView):
    template_name = "blossom/show.html"
    context_object_name = "current_events"
    
    def get_queryset(self):
        self.show = get_object_or_404(Show, id=self.kwargs["show_id"])
        return ShowEvent.objects.filter(show=self.show)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_id"] = self.show
        return context

class EventDetail(generic.DetailView):
    model = ShowEvent
    template_name = 'blossom/eventdetail.html'
    context_object_name = 'event'

class RoomEventList(generic.ListView):
    template_name = "blossom/rooms.html"
    context_object_name = "rooms"
    model = Location