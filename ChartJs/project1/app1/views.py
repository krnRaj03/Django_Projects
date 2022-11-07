from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
  #name list
  labels=[]
  #age list
  data=[]

  qs=person.objects.order_by('-age')[:5]
  for p in qs:
    labels.append(p.name)
    data.append(p.age)

  context={'labels':labels,'data':data}
  return render (request,'home.html',context)