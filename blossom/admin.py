from django.contrib import admin
from .models import ShowEvent, Location, Show

# Register your models here.
admin.site.register(ShowEvent)
admin.site.register(Location)
admin.site.register(Show)