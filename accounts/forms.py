from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
import datetime

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'type':'password'}))
    password2 = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'type':'password'}))
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cwid = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'type': 'number'}))
    dob = forms.DateField(widget = forms.SelectDateWidget(attrs={'class': 'browser-default'}))
    class_of = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'type': 'number'}))
    gender = forms.ChoiceField(choices=CHOICE, widget=forms.Select(attrs={'class': 'browser-default',}))
    class Meta:
        model = Profile
        fields = ('full_name', 'dob', 'address', 'cwid', 'class_of', 'gender', 'profile_picture', 'scanned_id')
