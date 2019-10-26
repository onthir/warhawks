from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def accounts_home(request):
    pass

'''
REGISTER NEW USER
#REGISTER ACCOUNT USING USER CREATION FORM WITH DEFAULT USER MODEL
'''

def register_account(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            form  = UserRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                credentials = form.save()

                # get username and password to login the user
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                new_user = authenticate(username=username, password=password)
                login(request, new_user)
                return redirect("accounts:complete_profile")
        else:
            form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

"""
COMPLETE USER PROFILE OR EDIT PROFILE BASED ON THE LOGIN OR REGISTER 
"""
def complete_profile(request):
    if request.user.is_authenticated:
        # get profile
        user = User.objects.get(username=request.user)
        try:
            profile = Profile.objects.get(user=user)
            if profile.started == True:
                return redirect("accounts:edit_profile")
            return redirect("accounts:edit_profile")

        except:
            pass
        msg = 'Complete your profile'
        # get profile form
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                pf = form.save(commit=False)
                pf.user = user
                pf.started = True
                pf.save()
                return redirect("main:home")
        else:
            form = ProfileForm()
        return render(request, 'accounts/cprofile.html', {'form': form, 'msg': msg})

@login_required
def edit_profile(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)

    # edit
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            pf = form.save()
            messages.success(request, 'Profile Updated Successfully')

    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/cprofile.html', {'form': form, 'msg':'Update Profile'})
'''
LOGIN USER 
LOGIN USER WITH THE DEFAULT USER MODEL AND THE AUTHENTICATE MODEL
'''

def login_user(request):

    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:home')
                else:
                    return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Invalid username or password'})
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect("accounts:login")

"""
DISPLAY USER PROFILE WITH CONTENTS LIKE PROFILE PICTURE, ID(PRIVATE), CWID(PRIVATE), POSTED CONTENT

"""
def display_profile(request, user):
    if request.user.is_authenticated:
        # get user and profile
        user = User.objects.get(username=user)
        profile = Profile.objects.get(user=user)

        # content for the logged in user
        context = {
            'user': user,
            'profile': profile
        }
        return render(request, 'accounts/profile.html', context)