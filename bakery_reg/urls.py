from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.main, name='main'),
    # path("register", views.register, name='register'),
    path('register/', views.CustomRegistrationView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bakery_reg/logout.html'), name='logout'),
]
