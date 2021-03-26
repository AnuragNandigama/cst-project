from django import forms
from .models import  StudentDetails, Profile

# class StudentDetailsForm(forms.Form):
    
#     COLLEGES = [
#         ('mcit', 'MCIT'),
#         ('tav', 'TAV'),
#         ('concordia', 'Concordia')
#     ]    
    
#     user_name = forms.CharField(label='Your Name', max_length=50, widget=forms.PasswordInput)
#     # user_college = forms.CharField(label='Your College', max_length='100')
#     user_college = forms.MultipleChoiceField(choices=COLLEGES, widget=forms.CheckboxSelectMultiple)
#     user_profile = forms.ChoiceField(label='Profile', choices=[('Local', 'Local Student'), ('International', 'International Student')])

class StudentDetailsForm(forms.ModelForm):
    # user_profile = forms.ModelChoiceField(empty_label=None, queryset=Profile.objects, widget=forms.RadioSelect)
    
    #image = forms.ImageField()    
    class Meta:
        model = StudentDetails
        fields = ['user_name', 'user_college', 'user_profile']
        labels = {'user_name': 'Name', 'user_college':'College'}
        widgets = {
            'user_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'user-college': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }),
            'user_profile':forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-control'
                    })            
            }
        
class MultipleUserInfoForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=5)
