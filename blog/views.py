from django.shortcuts import render

from .models import Blog

def allblogs(request):
    #get the blogs from the db here, then return them
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})
