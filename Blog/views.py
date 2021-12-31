from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

from App_Blog.models import Blog


def Index(request):
     blogs = Blog.objects.all()
     return render(request,'home.html',context={'blogs':blogs})
     #return HttpResponseRedirect(reverse('App_Blog:blog_list'))