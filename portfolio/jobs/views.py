from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Job, StudentDetails, Profile
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
            filled_form.save()
            message = "Your details have been captured. Thanks!"
            filled_form.cleaned_data['user_name']
            filled_form.cleaned_data['user_college']
            new_form = StudentDetailsForm()
            return render(request, 'jobs/user.html', {'studentform': new_form, 'message': message, 'multiple_form': multiple_form })
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
    
def user(request):
    student_data = StudentDetails.objects
    return render(request, 'jobs/user.html', {'students':student_data})

def edit_user(request, user_id):
    try:
        existing_data = get_object_or_404(StudentDetails, id=user_id)
    except Exception:
        raise Http404('Does not Exist')
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            data = StudentDetails.objects
            return render(request, 'jobs/user.html', {'students': data})
    else:
        form = StudentDetailsForm(instance=existing_data)
        return render(request, 'jobs/edit_user.html', {'form': form})


def delete_user(request, user_id):
    try:
        data = get_object_or_404(StudentDetails, id=user_id)
    except Exception:
        raise Http404('User does not exist')
    if request.method == 'POST':
        data.delete()
        data = StudentDetails.objects
        return render(request, 'jobs/user.html', {'students': data})
    else:
        return render(request, 'jobs/delete_user.html')