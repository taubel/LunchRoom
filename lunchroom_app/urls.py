from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('rooms/add/', views.RoomCreateView.as_view(), name="room-add"),
    path('rooms/<int:pk>/update/', views.RoomUpdateView.as_view(), name="room-update"),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name="room-delete"),
    path('rooms/<int:pk>/', views.RoomView.as_view(), name="room-get"),
]
