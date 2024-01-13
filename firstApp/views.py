from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def display(request):
    return HttpResponse("<h1>Hello World!</h1>")


def displaydatetime(request):
    dt = datetime.now()
    s = "<b>Current date time: </b>" + str(dt)
    return HttpResponse(s)
