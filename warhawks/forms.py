from django import forms
from .models import *

class AddStudyForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # study_material_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    study_material_type = forms.ModelChoiceField(queryset=M_type.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    file_content = forms.FileField(label='File',widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = StudyMaterial
        fields = ('study_material_type', 'title', 'description', 'file_content')

class AddJobForm(forms.ModelForm):
    j_type = forms.ModelChoiceField(label='Job Category', queryset=job_category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Name'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Job Position'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter Description'}))
    salary = forms.FloatField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01", 'placeholder': 'Enter Salary'}))
    class Meta:
        model = Job
        fields = ('j_type', 'company', 'position', 'description', 'salary')


# comment form for jobs
# JOBS COMMENT SECTION HERE JOB 

class JobCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your comment '}))
    class Meta:
        model = JobComment
        fields = ('comment',)

# ACCOMODATIONN FORM HERE
# ACCOMODATION

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('a_type', 'location', 'distance_from_university', 'price', 'description', 'picture')
