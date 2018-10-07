from django.urls import path

from . import views

urlpatterns = [
    #if someone is at /blog, then the allblog.html page is used
    path('', views.allblogs, name='allblogs'),
    #b/c of views.detail, I need a views function in views.py
    #if someone is at /blog/#, then the views.py is used then the...
    # detail.html page is used; int is saved as blog_id
    path('<int:blog_id>/', views.detail, name="detail"), 
] 
