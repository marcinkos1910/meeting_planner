from django.urls import path

from meetings import views

urlpatterns = [
    path('rooms', views.rooms_list, name='rooms'),
    path('meetings', views.meetings_list, name='meetings'),
    path('create_room', views.create_room, name='create_room'),
    path('create_meeting', views.create_meeting, name='create_meeting'),
]