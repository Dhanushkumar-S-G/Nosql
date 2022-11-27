from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("write_blog/",write_blog,name="write-blog"),
    path("read_blog/<int:id>",read_blog,name="read-blog"),
    path("view_blog/",view_blog,name="view-blog"),
    path("update_blog/<int:id>",update_blog,name="update-blog"),
    path("delete_blog/",delete_blogs,name="delete-blogs"),
    path("delete_blog/<int:id>",delete_blog,name="delete-blog"),
]
