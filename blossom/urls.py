from django.urls import path

from blossom.views.baseview import IndexView
from blossom.views.showview import ShowEvents,EventDetail,RoomEventList

app_name = 'blossom'
urlpatterns = [
    path("",IndexView.as_view(),name='index'),
    path("<int:show_id>/events",ShowEvents.as_view(),name='showdetail'),
    path("<int:show_id>/events/<pk>/",EventDetail.as_view(),name='eventdetail'),
    path("<int:show_id>/rooms/<pk>/",RoomEventList.as_view(),name='roomdetail')
]