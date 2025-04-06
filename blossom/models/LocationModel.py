from django.db import models
from .ShowModel import Show

class Location(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    eventlocation = models.ForeignKey(Show, on_delete=models.CASCADE)