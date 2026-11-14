from datetime import date
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound 
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

# =======================================================================

# 1)) To make code dynamic we can make dictionary like below :


blog_details = [
    
    {
        "slug" : "python-intro",
        "image" : "img1.jpg",
        "date" : date(2026,11,14),
        "title" : "Python Introduction",
        "preview" : """ 
            Python is an open source, high-level interpreted programming language used widely. Application of python are web development, data science, machine learning, artificial intelligence, automation, and many more.    
        """,
        "content" : """ 
            Python is a high-level, easy‑to‑read programming language with simple syntax and broad applications.Created by Guido van Rossum and released in 1991, it supports multiple programming paradigms and runs on Windows, macOS, Linux, and more. You can start coding instantly with a “Hello, World!”
        """
    },
    {
        "slug" : "python-oops",
        "image" : "img2.jpg",
        "date" : date(2026,11,13),
        "title" : "Object Oriented Programming with Python",
        "preview" : """
            object oriented programming is a fundamental programming paradigm that uses objects and classes to structure code.
        """,
        "content" : """
            OOP is a way of organizing code that uses concept of classes and objects to represent real-world entities and their interactions. It promotes code reusability, modularity, and encapsulation, making it easier to manage complex software systems.
        """
    },
    {
        "slug" : "django-basics",
        "image" : "img3.jpg",
        "date" : date(2026,11,11),
        "title" : "Basics of Django framework of Python",
        "preview" : """Django is a Python-based web framework that simplifies building secure, scalable, and maintainable web applications using the Model‑View‑Template (MVT) architecture""" ,
        "content" : """ 
            Django is free, open-source, and follows the DRY (Don’t Repeat Yourself) principle. It handles many backend tasks — database management, user authentication, URL routing, form handling — so you can focus on application logic 
            . It works with SQLite, MySQL, and PostgreSQL, and includes a built‑in admin panel for easy data management
        """
    },
    {
        "slug" : "regex",
        "image" : "img4.jpg",
        "date" : date(2026,11,10),
        "title" : "Regular Expressions in Python",
        "preview" : """
                    In Python, a regular expression is a sequence of characters         that defines a search pattern, used for matching, validating, or extracting      text via the re module. 
        """,
        "content" : """
                    Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python and made available through the re module. Using this little language, you specify the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like.
        """
    }
]

# {
#     "python-intro" : "Introduction to Python" ,
#     "python-oops" : "object oriented programming with python" ,
#     "django-basics" : "Basics of Django" ,
#     "regex" : "Regular expressions" ,
#     "tkinter" : None
# }

# =======================================================================

def blogposts(request):
    
    return render(request, "blogs/allposts.html", {"blogs" : blog_details} )
    # list_items = ""
    # blog_list = list(blog_names.keys()) 
    
    
    # for b in blog_list:
    #     blog_path = reverse("blog-post", args=[b]) # reverse function of Python not Django...
    #     list_items += f'<li> <a href="{blog_path}"> {b.capitalize()} </a> </li>'    

    # 1) below is a static method :
    # res_data = """ # this can also be dynamic. See above statements for that                                                                               
    # <ul>
    #     <li> <a href = "blogposts/python-intro"> Python Introduction </a> </li>
    #     <li> <a href = "blogposts/python-oops"> Object Oriented Programming with Python </a> </li>
    #     <li> <a href = "blogposts/python-oops"> Basics of Django </a> </li>
    # </ul>        
    # return HttpResponse(res_data)
    # """
    
    # 2) below is a dynamic method
    
    # res_data = f"<ul> {list_items} </ul>"
    # return HttpResponse(res_data)
    
    # return HttpResponse("<h1>All blog posts !</h1>")

def home(request):
    sorted_blogs = sorted(blog_details, key=lambda post:post['date'], reverse=True)
    latest_blogs = sorted_blogs[:2]
    return render(request, "blogs/index.html", {"latestBlogs" : latest_blogs})   

# def python_intro(request):
#     return HttpResponse("Introduction to Python")

# def python_oops(request):
#     return HttpResponse("object oriented programming with python")

# def django_basics(request):
#     return HttpResponse("basics of Django")


def process_blog_names(blog):
    blog_list = blog.split("-")
    # return " ".join(blog_list).title()
    return " ".join(blog_list) # we added title functionality in our template. see the blogs.html file 


# 2)) this is long method, bacause we are adding elif statements for urls. If there are 100 urls then we need to add 100 if...elilf..else statements.

def blogs(request, blog):
    
    # if blog == "python-intro":
    #     res = "introduction to python"
    # elif blog == "python-oops":
    #     res = "object oriented programming with python"
    # elif blog == "django-basics":
    #     res = "basics of django"
    # else: 
    
    # ===========================================================
    # lets make it more dynamic
    
    # ===========================================================
    
    try:
        res = blog_names[blog]
        return render(request, "blogs/blogs.html", {"blog_text" : res , "blog_name" : process_blog_names(blog)})
    except Exception:
        # res_data = render_to_string("404.html")
        # return HttpResponseNotFound(res_data)
        raise Http404()
    # else:
    #     return HttpResponse(res)

def blog_posts_by_numbers(request, blog):
    return HttpResponse(blog)