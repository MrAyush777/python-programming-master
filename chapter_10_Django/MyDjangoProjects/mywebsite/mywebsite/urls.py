"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# below are project level urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('blogs/',include('blogs.urls')) # This is a blogs page not the home page. when we run the server it is by default run on home page. and the url of actual homepage is : http://127.0.0.1:8000. 
    # so to make that remove 'blogs/' from the above url
    
    path('', include('blogs.urls'))
]
