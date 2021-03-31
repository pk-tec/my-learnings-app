"""Defines URL patterns for users"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Includes default auth urls. 
    path('', include('django.contrib.auth.urls')),
]