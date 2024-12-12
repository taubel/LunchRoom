from django.urls import path

from .views import HomeView, RoomView


urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('room/<int:pk>/', RoomView.as_view(), name="room"),
]
