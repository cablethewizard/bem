from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=250)
    starttime = models.DateTimeField("start time")
    endtime = models.DateTimeField("end time")
    description = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=False)