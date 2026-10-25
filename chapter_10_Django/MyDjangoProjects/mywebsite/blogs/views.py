from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 
# Create your views here.

def blogposts(request):
    return HttpResponse("<h1>All blog posts !</h1>")

def home(request):
    return HttpResponse("<h1>HOME PAGE</h1>")

# def python_intro(request):
#     return HttpResponse("Introduction to Python")

# def python_oops(request):
#     return HttpResponse("object oriented programming with python")

# def django_basics(request):
#     return HttpResponse("basics of Django")

# 1) To make code dynamic we can make dictionary like below :

blog_names = {
    "python-intro" : "<h1> Introduction to Python </h1>" ,
    "python-oops" : "<h1> object oriented programming with python </h1>" ,
    "django-basics" : "<h1> Basics of Django </h1>" ,
    "regex" : "<h1> Regular expressions </h1>"
}

# 2) this is long method, bacause we are adding elif statements for urls. If there are 100 urls then we need to add 100 if...elilf..else statements.

def blogs(request, blog):
    
    # if blog == "python-intro":
    #     res = "introduction to python"
    # elif blog == "python-oops":
    #     res = "object oriented programming with python"
    # elif blog == "django-basics":
    #     res = "basics of django"
    # else: 
    
    try:
        res = blog_names[blog]
    except Exception:
        return HttpResponseNotFound("<h1>Page Not found</h1>")
    else:
        return HttpResponse(res)



def blog_posts_by_numbers(request, blog):
    return HttpResponse(blog)