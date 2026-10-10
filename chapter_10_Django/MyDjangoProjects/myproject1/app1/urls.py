# This file contains the list of URLs that you want to support along with the view function.

from django.urls import path
from . import views

# this function gets two arguments : 1) URL as string 2) function names. Here we don't need to call this function, the django will take care of this. 

urlpatterns = [
    path("blogs", views.blogs) # Here we are telling django that if a request is made to the url /blogs 
]