from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Room, User


class RoomListView(ListView):
    model = Room


class RoomDetailView(DetailView):
    model = Room

    def get_context_data(self, **kwargs):
        users = [user for user in self.get_object().users.all()]
        return {
            "object": self.get_object(),
            "users": users
            }


class RoomCreateView(CreateView):
    model = Room
    fields = ["patron", "users"]


class RoomUpdateView(UpdateView):
    model = Room
    fields = ["patron", "users"]


class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy("rooms")


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = ["name"]


class UserUpdateView(UpdateView):
    model = User
    fields = ["name"]


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("users")
