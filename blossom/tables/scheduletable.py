import django_tables2 as tables
from blossom.models.ShowModel import Show
from blossom.models.EventModel import ShowEvent
from blossom.models.LocationModel import Location

class RoomSchedule(tables.Table):
    name = tables.Column()
    starttime = tables.TimeColumn()
    endtime = tables.TimeColumn()
    date = tables.DateColumn()
    class Meta:
        template_name = 'django_tables2/bootstrap.html'