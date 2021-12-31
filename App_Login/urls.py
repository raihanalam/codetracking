from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.sign_in,name='signin'),
    path('signout/',views.sign_out,name='signout'),
    path('profile/',views.user_profile,name='profile'),
    path('change-profile/',views.change_profile,name='change_profile'),
    path('password/',views.change_password,name='change_password'),
    path('add-picture/',views.add_pro_pic,name='add_pro_pic'),
    path('change-picture/',views.change_pro_pic,name='change_pro_pic'),
]

