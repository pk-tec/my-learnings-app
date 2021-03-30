"""Define URL pattern for my_learning."""
from django.urls import path
from . import views

app_name = 'my_learning'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]