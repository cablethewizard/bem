from django.urls import path
from .views import *

app_name = 'blossom'
urlpatterns = [
    path("",index,name='index'),
    path("<int:show_id>/", showdetail,name='showdetail' )
]