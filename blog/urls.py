from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("write_blog/",write_blog,name="write-blog"),
    path("update_blog/",update_blog,name="update-blog"),
    path("delete_blog/",delete_blog,name="delete-blog"),
]