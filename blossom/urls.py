from django.urls import path

from blossom.views.baseview import IndexView
from blossom.views.showview import EventDetail
from blossom.views.showview import RoomEventList
from blossom.views.showview import roomListView

app_name = 'blossom'
urlpatterns = [
    path("",IndexView.as_view(),name='index'),
    path("<int:show_id>/events",roomListView,name='showdetail'),
    path("<int:show_id>/events/<pk>/",EventDetail.as_view(),name='eventdetail'),
    path("<int:show_id>/rooms/<pk>/",RoomEventList.as_view(),name='roomdetail')
]