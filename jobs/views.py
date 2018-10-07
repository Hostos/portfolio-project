from django.shortcuts import render

from .models import Job

def home(request):
    #get the jobs from the db here, then return them
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

