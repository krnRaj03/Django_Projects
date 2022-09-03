from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login


x=[] 
def index(request):
    program = Programming.objects.all()
    return render(request,'index.html',{'program': program})

def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'results.html', {'courses': courses, })


