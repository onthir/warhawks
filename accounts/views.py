from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ProfileForm, EditProfileForm
from .models import Profile


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

                # create profile
                
                dob = request.POST.get('dob')
                address = request.POST.get('address')
                class_of = request.POST.get('class_of')
                cwid = request.POST.get('cwid')
                full_name = request.POST.get('full_name')

                print(dob)
                # get username and password to login the user
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                new_user = authenticate(username=username, password=password)
                login(request, new_user)
                return redirect("main:home")
        else:
            form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

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

# profile for the user extended with the user model
def complete_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.started = True
                profile.save()

                return redirect("main:home")
        else:
            form = ProfileForm()
        return render(request, 'accounts/complete-profile.html', {'form': form})
        

        