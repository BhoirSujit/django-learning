from django import forms

class UserRegistrationForm(forms.Form):
    firstname= forms.CharField()
    lastname= forms.CharField()
    email = forms.EmailField()