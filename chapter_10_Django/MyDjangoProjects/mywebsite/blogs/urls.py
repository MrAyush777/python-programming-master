from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("blogposts",views.blogposts),

    # static path - below all are static paths of all blog posts 

    # path("allposts/python-intro", views.python_intro),
    # path("allposts/python-oops", views.python_oops),
    # path("allposts/django-basics", views.django_basics),

    # dynamic path - below is a dynamic path for all blog posts
    
    path("blogposts/<blog>", views.blogs)
    
]