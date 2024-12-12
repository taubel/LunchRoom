from django.shortcuts import render

from .models import Room


def home(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "lunchroom_app/index.html", context=context)


def single_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    return render(request, "lunchroom_app/room.html", context={"room": room})
