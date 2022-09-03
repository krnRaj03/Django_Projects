from django.shortcuts import render
from .forms import *
from datetime import datetime

# Create your views here.

def home(request):
  form=testForm(request.POST)
  if form.is_valid():
    na = form.cleaned_data['name']
    st = form.cleaned_data['startdate']
    en=form.cleaned_data['enddate']
    tot=en-st
    
    print(tot,na,st,en)
    form.save()
  
  return render(request, 'index.html',{'form':form,'tot':tot})