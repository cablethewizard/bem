from django.contrib import admin
from blossom.models.EventModel import ShowEvent
from blossom.models.LocationModel import Location
from blossom.models.ShowModel import Show

# Register your models here.
admin.site.register(ShowEvent)
admin.site.register(Location)
admin.site.register(Show)