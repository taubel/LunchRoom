from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Room


class HomeView(ListView):
    model = Room


class RoomView(DetailView):
    model = Room
