from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job
from .forms import StudentDetailsForm, MultipleUserInfoForm
from django.forms import formset_factory

# Create your views here.
def basepage(request):
    return render(request, 'jobs/base.html')

def homepage(request):
    #return HttpResponse("Hello CST Team, you've reached Home Page of Jobs app")
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def user(request):
    return render(request, 'jobs/user.html')

def summary(request):
    jobs = Job.objects
    return render(request, 'jobs/summary.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})

def contact(request):
    multiple_form = MultipleUserInfoForm()
    if request.method == 'POST':
        filled_form = StudentDetailsForm(request.POST, request.FILES)
        if filled_form.is_valid():
            message = "Your details have been captured. Thanks!"
            filled_form.cleaned_data['user_name']
            filled_form.cleaned_data['user_college']
            new_form = StudentDetailsForm()
            return render(request, 'jobs/contact.html', {'studentform': new_form, 'message': message, 'multiple_form': multiple_form })
    else:   
        form = StudentDetailsForm()
        return render(request, 'jobs/contact.html', {'studentform': form, 'multiple_form': multiple_form})
    
def blog(request):
    number_of_users = 2
    filled_multiple_user_form = MultipleUserInfoForm(request.GET)
    if filled_multiple_user_form.is_valid():
        number_of_users = filled_multiple_user_form.cleaned_data['number']
    UserInfoFormSet = formset_factory(StudentDetailsForm, extra=number_of_users)
    formset = UserInfoFormSet()
    if request.method == "POST":
        filled_formset = UserInfoFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data["user_name"])
            note = "Users have been registered"
        else:
            note = "User has not been registered!"
        return render(request, 'jobs/blog.html', {'note':note, 'formset': formset}) 
    else:
        return render(request, 'jobs/blog.html', {'formset': formset}) 
    
    

        

    