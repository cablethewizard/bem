from django.db import models
from .LocationModel import Location
from .ShowModel import Show

class ShowEvent(models.Model):
    name = models.CharField(max_length=250)
    starttime = models.DateTimeField("start time")
    endtime = models.DateTimeField("end time")
    description = models.TextField(blank=True, null=True)
    room = models.ForeignKey(Location, on_delete=models.DO_NOTHING,null=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE,null=True)