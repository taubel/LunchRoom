from django.shortcuts import render

from .models import Room


def room(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "lunchroom_app/index.html", context=context)
