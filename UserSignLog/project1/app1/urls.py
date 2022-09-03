from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('signup',views.signup, name='signup'),
]
