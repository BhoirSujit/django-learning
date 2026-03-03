from django.shortcuts import render
from . import forms

# Create your views here.
def UserRegistrationView(req):
    form = forms.UserRegistrationForm()
    return render(req, 'formDemo/userRegistration.html', {'form' : form})