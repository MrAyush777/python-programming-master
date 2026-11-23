from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Post

# Create your views here.

# =======================================================================

def blogposts(request):
    
    blog_details = Post.objects.all()
    return render(request, "blogs/allposts.html", {"blogs" : blog_details} )
    
    
def home(request):
   
    latest_blogs = Post.objects.all().order_by("-date")[:2]
    return render(request, "blogs/index.html", {"latestBlogs" : latest_blogs})   


def blogs(request, blog):
    try:
        res = Post.objects.get(slug=blog) # here slug is a field in our Post model. we can use any field to get the data from database.
        return render(request, "blogs/blogs.html", {"post" : res})
    except Exception:
        raise Http404()
  

def blog_posts_by_numbers(request, blog):
    return HttpResponse(blog)