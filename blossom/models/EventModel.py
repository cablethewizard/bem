from optparse import check_builtin
from django.db import models
from django.forms import ValidationError
from .LocationModel import Location
from .ShowModel import Show

class ShowEvent(models.Model):
    name = models.CharField(max_length=250)
    starttime = models.TimeField("Start Time")
    endtime = models.TimeField("End Time")
    description = models.TextField(blank=True, null=True)
    room = models.ForeignKey(Location, on_delete=models.DO_NOTHING,null=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE,null=True)
    date = models.DateField("Event Date")


    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #inner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outer limits
            overlap = True
    
    def check_inshow(self, showstart, showend):
        inshow = True
        if showstart > self.date:
            inshow = False
        elif showend < self.date:
            inshow = False


    def clean(self):
        if self.endtime <= self.starttime:
            raise ValidationError('End time must be after start time')
        
        if self.check_inshow(self.show.startdate, self.show.enddate):
            raise ValidationError({'date':'Event date not within show date range'})

        roomevents = ShowEvent.objects.filter(room=self.room)
        if roomevents.exists():
            for event in roomevents:
                if self.check_overlap(event.starttime,event.endtime,self.starttime,self.endtime):
                    raise ValidationError(
                            'There is an overlap with another event: ' + str(event.day) + ', ' + str(event.start_time) + '-' + str(event.end_time))