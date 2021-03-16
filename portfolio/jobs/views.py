from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job

# Create your views here.
def basepage(request):
    return render(request, 'jobs/base.html')

def homepage(request):
    #return HttpResponse("Hello CST Team, you've reached Home Page of Jobs app")
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def contact(request):
    return render(request, 'jobs/contact.html')

def summary(request):
    jobs = Job.objects
    return render(request, 'jobs/summary.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})