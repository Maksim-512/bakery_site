from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.main, name='new_main'),
    path("user_profile", views.profile_list, name='profile')
    ]
