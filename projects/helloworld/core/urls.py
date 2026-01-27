from django.urls import path
from core.views import home, displyDateTime


urlpatterns = [
    path("", home),
    path("time/", displyDateTime),
]
