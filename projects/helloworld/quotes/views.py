from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showQuotes(req):
    return HttpResponse("Bona fir bhi bona hai chahe wo parawat pe bhi kyu na khada ho")