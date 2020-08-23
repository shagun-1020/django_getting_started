from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Meeting, Room
from .forms import MeetingForm


# Create your views here.
def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request,"meetings/detail.html",{"meeting": meeting})


def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request,"meetings/roomDetail.html",{"room": room})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
