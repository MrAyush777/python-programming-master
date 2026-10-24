from django.urls import path
from . import views

# below are app level urls

urlpatterns = [
    
    path("",views.home),
    path("blogposts",views.blogposts),

    # static path - below all are static paths of all blog posts 

    # path("allposts/python-intro", views.python_intro),
    # path("allposts/python-oops", views.python_oops),
    # path("allposts/django-basics", views.django_basics),

    # dynamic path - below is a dynamic path for all blog posts
    # remember that the order of this segmens/paths are also important, as when it call the function it follos the FIFO approach

    # **** path convertor **** : 

    # 1) METHOD 1 - data types : it uses data types like below, it separates 

    # path("blogposts/<int:blog>", views.blog_posts_by_numbers), # path convertors
    # path("blogposts/<str:blog>", views.blogs) # path convertors
    
    # 2) METHOD 2 - slug : it accepts alphabets, numbers and hyphen in the url and nothig else.
    
    path("blogposts/<slug:blog>", views.blogs)
]