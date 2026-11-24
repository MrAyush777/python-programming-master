from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Post
from .forms import CommentForm

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
        post_data = Post.objects.get(slug=blog) # here slug is a field in our Post model. we can use any field to get the data from database.
        tag_caption = post_data.tags.all()
        form_data = CommentForm()
        return render(request, "blogs/blogs.html", 
            {"post" : post_data, "tags" : tag_caption, "comment_form" : form_data})
    except Exception:
        raise Http404()
  