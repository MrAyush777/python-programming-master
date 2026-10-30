from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

# 1)) To make code dynamic we can make dictionary like below :

blog_names = {
    "python-intro" : "Introduction to Python" ,
    "python-oops" : "object oriented programming with python" ,
    "django-basics" : "Basics of Django" ,
    "regex" : "Regular expressions"
}

def blogposts(request):
    
    list_items = ""
    blog_list = list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse("blog-post", args=[b])
        list_items += f'<li> <a href="{blog_path}"> {b.capitalize()} </a> </li>'    

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
    
    res_data = f"<ul> {list_items} </ul>"
    return HttpResponse(res_data)
    
    # return HttpResponse("<h1>All blog posts !</h1>")

def home(request):

    return render(request, "blogs/index.html")   
    # res_data = render_to_string("blogs/index.html")
    # return HttpResponse(res_data)

# def python_intro(request):
#     return HttpResponse("Introduction to Python")

# def python_oops(request):
#     return HttpResponse("object oriented programming with python")

# def django_basics(request):
#     return HttpResponse("basics of Django")


def process_blog_names(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list).title()


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
        return HttpResponseNotFound("<h1>Page Not found</h1>")
    # else:
    #     return HttpResponse(res)



def blog_posts_by_numbers(request, blog):
    return HttpResponse(blog)