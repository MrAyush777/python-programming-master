from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 
# Create your views here.

def blogposts(request):
    return HttpResponse("All blog posts !")

def home(request):
    return HttpResponse("HOME PAGE")

# def python_intro(request):
#     return HttpResponse("Introduction to Python")

# def python_oops(request):
#     return HttpResponse("object oriented programming with python")

# def django_basics(request):
#     return HttpResponse("basics of Django")

def blogs(request, blog):
    
    if blog == "python-intro":
        res = "introduction to python"
    elif blog == "python-oops":
        res = "object oriented programming with python"
    elif blog == "django-basics":
        res = "basics of django"
    else:
        return HttpResponseNotFound("Page Not found")
    return HttpResponse(res)

def blog_posts_by_numbers(request, blog):
    return HttpResponse(blog)