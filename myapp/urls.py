from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='index'),
    path('home/',views.homepg,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
]
