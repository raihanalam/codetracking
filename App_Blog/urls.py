
from django.contrib import admin
from django.urls import path,include
from django.views.generic.edit import UpdateView
from . import views
app_name = 'App_Blog'

urlpatterns = [
    path('',views.BlogList.as_view(),name='blog_list'),
    path('write/',views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>',views.blog_details, name='blog_details'),
    path('liked/<pk>/',views.liked, name='liked_post'),
    path('unliked/<pk>/',views.unliked, name='unliked_post'),
    path('my-blogs/',views.MyBlogs.as_view(),name='my_blogs'),
    path('edit/<pk>',views.UpdateBlog.as_view(),name='edit_blog'),
    path('delete/<pk>',views.delete_blog,name='delete_blog'),
]
