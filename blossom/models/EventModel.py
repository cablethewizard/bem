from django.db import models
from django.forms import ValidationError
from .LocationModel import Location
from .ShowModel import Show

class ShowEvent(models.Model):
    name = models.CharField(max_length=250)
    starttime = models.DateTimeField("start time")
    endtime = models.DateTimeField("end time")
    description = models.TextField(blank=True, null=True)
    room = models.ForeignKey(Location, on_delete=models.DO_NOTHING,null=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE,null=True)

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #inner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outer limits
            overlap = True

    def clean(self):
        if self.endtime <= self.starttime:
            raise ValidationError('End time must be after start time')
        
        roomevents = ShowEvent.objects.filter(room=self.room)
        if roomevents.exists():
            for event in roomevents:
                if self.check_overlap(event.starttime,event.endtime,self.starttime,self.endtime):
                    raise ValidationError(
                            'There is an overlap with another event: ' + str(event.day) + ', ' + str(event.start_time) + '-' + str(event.end_time))