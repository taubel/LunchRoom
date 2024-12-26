from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="lunchroom_app/index.html"), name="index"),

    path('rooms/', views.RoomListView.as_view(), name="rooms"),
    path('rooms/add/', views.RoomCreateView.as_view(), name="room-add"),
    path('rooms/<int:pk>/update/', views.RoomUpdateView.as_view(), name="room-update"),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name="room-delete"),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name="room-get"),

    path('users/', views.UserListView.as_view(), name="users"),
    path('users/add/', views.UserCreateView.as_view(), name="user-add"),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name="user-update"),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name="user-delete"),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name="user-get"),
]
