from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Room


class HomeView(ListView):
    model = Room


class RoomView(DetailView):
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
    success_url = reverse_lazy("index")
