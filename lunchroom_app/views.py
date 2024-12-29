from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse

from .forms import FoodItemForm
from .models import Room, User, FoodItem


class RoomListView(ListView):
    model = Room


class RoomDetailView(DetailView):
    model = Room

    def get_context_data(self, **kwargs):
        foods = [food for food in self.get_object().foods.all()]
        return {
            "object": self.get_object(),
            "users": self.get_object().users,
            "foods": foods,
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


def fooditem_add(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse_lazy("room-get", kwargs={"pk": form.cleaned_data["room"].id})
            return HttpResponseRedirect(url)
    else:
        form = FoodItemForm()
    return render(request, "lunchroom_app/fooditem_form.html", {"form": form})
