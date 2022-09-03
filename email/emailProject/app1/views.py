from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
  if request.method=="POST":
    send_mail(
      'from HR:',
      'Hi! Welcome to our company.',
      'krnraj002@gmail.com',
      ['krnraj07@gmail.com','vusala.devil@gmail.com'],
    )

  return render(request,'index.html')