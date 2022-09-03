from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import registerform
from django.contrib.auth import login, logout, authenticate
from django.conf import settings



# Create your views here.
def base(request):
  return render(request,'base.html')

def home(request):
  return render(request,'home.html')

def signup(request):
  if request.method=='POST':
    form=registerform(request.POST)
    if form.is_valid():
      user=form.save()
      login(request,user)
      send_mail(
      'Subject here',
      'Here is the message.',
      settings.EMAIL_HOST_USER,
      ['krnmod03@gmail.com'],
      fail_silently=False,
      )
    return redirect('/login')            
  else:
    form=registerform()

  return render(request,'registration/signup.html',{'form1':form})