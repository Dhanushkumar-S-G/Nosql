from django.shortcuts import render
from django.http import HttpResponse 
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,"blog/home.html",{"blogs":blogs,"user":"Dhanushkumar S G"})

def write_blog(request):
    return HttpResponse("write blog")

def update_blog(request):
    return HttpResponse("update page")

def delete_blog(request):
    return HttpResponse("delete blog")