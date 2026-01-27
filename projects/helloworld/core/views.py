from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request) :
    return HttpResponse("Hello user, welcome to Django")

def displyDateTime(req):
    dt = datetime.datetime.now()
    s = "<b>Current Date and Time: </b>" + str(dt)
    return HttpResponse(s)
