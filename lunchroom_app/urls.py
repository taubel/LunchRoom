from django.urls import path

from .views import home, single_room


urlpatterns = [
    path('', home, name="index"),
    path('room/<int:room_id>/', single_room, name="room"),
]
