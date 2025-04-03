from django.urls import path
from .views import index,showdetail

app_name = 'blossom'
urlpatterns = [
    path("",index,name='index'),
    path("<int:show_id>/", showdetail,name='showdetail' )
]