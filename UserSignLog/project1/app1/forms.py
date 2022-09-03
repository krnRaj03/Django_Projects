from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registerform(UserCreationForm):
  email= forms.EmailField(required=False)
  phonenumber=forms.IntegerField(required=False)

  class Meta():
    model=User
    fields=['username','email','phonenumber','password1','password2']