from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=250)
    startdate = models.DateField("Start Date",null=True)
    enddate = models.DateField("End Date",null=True)
    description = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=False)