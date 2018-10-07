from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    #get the blogs from the db here, then return them
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

#returns/displays all the info of a particular blog entry
def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})