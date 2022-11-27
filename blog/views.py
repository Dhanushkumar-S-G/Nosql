from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Blog
from .forms import CreateBlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,"blog/home.html",{"blogs":blogs,"user":"Dhanushkumar S G"})

def write_blog(request):
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateBlogForm()
    return render(request,"blog/write_blog.html",{"form":form})

def update_blog(request,id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        form = CreateBlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateBlogForm(instance=blog)
    return render(request,"blog/write_blog.html",{"form":form})

def delete_blog(request,id):
    blog =  Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')

def delete_blogs(request):
    blogs = Blog.objects.all()
    return render(request,"blog/delete_blogs.html",{"blogs":blogs,"user":"Dhanushkumar S G"})
    

def read_blog(request,id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/read_blog.html",{"blog":blog,"user":"Dhanushkumar S G"})

def view_blog(request):
    blogs = Blog.objects.all()
    return render(request,"blog/view_blogs.html",{"blogs":blogs,"user":"Dhanushkumar S G"})
