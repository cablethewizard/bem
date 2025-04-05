from django.urls import path

from .views import IndexView,ShowEvents,EventDetail,RoomEventList

app_name = 'blossom'
urlpatterns = [
    path("",IndexView.as_view(),name='index'),
    path("<int:show_id>/events",ShowEvents.as_view(),name='showdetail'),
    path("<int:show_id>/events/<pk>/",EventDetail.as_view(),name='eventdetail'),
    path("<int:show_id>/rooms",RoomEventList.as_view(),name='roomdetail')
]