from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting, Room


def welcome(request):
    return render(request,"website/welcome.html",
                  {"meetings": Meeting.objects.all(),
                   "rooms": Room.objects.all()})


def about(request):
    return HttpResponse("Hi I am Shagun. I am learning Django")

# Create your views here.
