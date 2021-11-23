from django.shortcuts import render, redirect

from meetings.forms import MeetingForm, RoomForm
from meetings.models import Room, Meeting


def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/room_list.html', {"rooms": rooms})


def meetings_list(request):
    rooms = Meeting.objects.all()
    return render(request, 'meetings/meeting_list.html', {"rooms": rooms})


def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RoomForm()

    return render(request, 'meetings/create_room.html', {"form": form})


def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()

    return render(request, 'meetings/create_meeting.html', {"form": form})
