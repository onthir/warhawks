from django import forms
from .models import *



class AddJobForm(forms.ModelForm):
    j_type = forms.ModelChoiceField(queryset=job_category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Name'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Job Position'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea', 'placeholder': 'Enter Description'}))
    salary = forms.FloatField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01", 'placeholder': 'Enter Salary'}))
    
    class Meta:
        model = Job
        fields = ('j_type', 'company', 'position', 'description', 'salary')


# comment form for jobs
# JOBS COMMENT SECTION HERE JOB 

class JobCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your comment ', }))
    class Meta:
        model = JobComment
        fields = ('comment',)
#job edit form
# EDIT JOB FORM
class EditJobForm(forms.ModelForm):
    j_type = forms.ModelChoiceField(queryset=job_category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Name'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Job Position'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea', 'placeholder': 'Enter Description'}))
    salary = forms.FloatField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01", 'placeholder': 'Enter Salary'}))
    
    class Meta:
        model = Job
        fields = ('j_type', 'company', 'position', 'description', 'salary', )



# ACCOMODATIONN FORM HERE
# ACCOMODATION

class ApartmentForm(forms.ModelForm):
    a_type = forms.ModelChoiceField(queryset=a_type.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea', 'placeholder': 'Enter Description'}))
    
    class Meta:
        model = Apartment
        fields = ('a_type', 'location', 'distance_from_university', 'price', 'description', 'picture')

# apartment comment form
class ApartmentCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your comment ', 'autocomplete':'off', 'autofocus':'on'}))
    class Meta:
        model = ApartmentComment
        fields = ('comment', )
# edit apartment form
class EditApartmentForm(forms.ModelForm):
    a_type = forms.ModelChoiceField(queryset=a_type.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea', 'placeholder': 'Enter Description'}))
   
    class Meta:
        model = Apartment
        fields = ('a_type', 'location', 'distance_from_university', 'price', 'description', 'picture')


class AddStudyForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    study_material_type = forms.ModelChoiceField(queryset=M_type.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}))
    file_content = forms.FileField(label='File',widget=forms.ClearableFileInput(attrs={'multiple': True, 'class':'file-field input-field fileinput'}))
    class Meta:
        model = StudyMaterial
        fields = ('study_material_type', 'title', 'description', 'file_content', 'preview_picture')


# ADD LOST AND FOUND REPORT FORM
class LostandFoundForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=LFCategory.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea', 'placeholder':'Enter Description of the found or lost item.'}))
    found_or_lost_on = forms.DateField(widget = forms.TextInput(attrs={'class': 'datepicker', 'placeholder':'Date When you found or lost the item', 'data-value': '2018/01/01'}))
    class Meta:
        model = LostAndFound
        fields = ('category', 'title', 'description', 'image','found_or_lost_on', )

# lost and found comment form
class LFCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your comment ', 'autocomplete':'off', 'autofocus':'on'}))
    class Meta:
        model = LFComment
        fields = ('comment', )