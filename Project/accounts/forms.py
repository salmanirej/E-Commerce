from django import forms
from . import models
from django.contrib.auth.models import  User

class userform(forms.ModelForm):
    class meta:
        model=User
        fields={'username','first_name','last_name','email'}

class ProfileForm(forms.ModelForm):
    class meta:
     model=models.Profile
     fields={'image','country','address'}

