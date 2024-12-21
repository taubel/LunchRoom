from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Room


class HomeView(ListView):
    model = Room


class RoomView(DetailView):
    model = Room


class RoomCreateView(CreateView):
    model = Room
    fields = ["patron"]


class RoomUpdateView(UpdateView):
    model = Room
    fields = ["patron"]


class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy("index")
