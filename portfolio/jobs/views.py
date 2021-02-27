from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Hello CST Team, you've reached Home Page of Jobs app")
    #return render(request, 'jobs/home.html')

def contact(request):
    return HttpResponse("Contact montrealcollege.ca for further info about the CST program")

