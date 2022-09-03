from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.index,name='index'),
    path('load-courses/', views.load_courses, name='ajax_load_courses'),
]
