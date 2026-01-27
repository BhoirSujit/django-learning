from django.urls import path
from quotes.views import showQuotes


urlpatterns = [
    path("", showQuotes),
]
