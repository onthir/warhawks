from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import AddStudyForm, AddJobForm, JobCommentForm, ApartmentForm
from django.contrib.auth.decorators import login_required
from blog.models import *
from accounts.models import *

""" THIS IS THE HOME PAGE WHERE TOP FOUR CHOICES OF JOBS, APARTMENTS AND BLOGS ARE DISPLAYED
ALSO SOME OTHER CONTENT ARE DISPLAYED

/* HOME */

"""
def home(request):
    jobs = Job.objects.all()[:4]
    apartments = Apartment.objects.all()[:4]
    recent_three = Blog.objects.all().order_by('-posted_on')[:3]
    four_blogs = Blog.objects.all().order_by('-posted_on')[:4]

    # profile
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = None
    context = {
        'jobs': jobs,
        'apartments': apartments,
        'nbar': 'home',
        'recent_three': recent_three,
        'four_blogs': four_blogs,
        'profile': profile
    }
    return render(request, 'warhawks/index.html', context)



"""

------------------------
JOB SECTION - Job Home, Add Jobs, Add job comment and details handling
------------------------
"""
# jobs home page with all the job listings
def job_listings(request):
    jobs = Job.objects.all()
    count_job = jobs.count()
    context = {
        'jobs': jobs,
        'count_job': count_job,
        'nbar': 'job_listings'
    }
    return render(request, 'warhawks/jobs.html', context)

# add jobs
@login_required
def add_jobs(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.hits = 0
            job.save()
            return redirect("main:job_listings")
    else:
        form = AddJobForm()
    return render(request, 'warhawks/addjob.html', {'form': form, 'nbar': 'job_listings'})

def job_details(request, slug):
    job = Job.objects.get(slug=slug)
    comments = JobComment.objects.all().order_by('-date').filter(job=job)
    if request.method == 'POST':
        form = JobCommentForm(request.POST or None)
        if form.is_valid():
            com = form.save(commit=False)
            com.job = job
            try:
                com.user = request.user
                com.save()
                return HttpResponseRedirect('/job-details/%s/' %slug)
            except:
                return redirect("accounts:login")
    else:
        form = JobCommentForm()

    context = {
        'job': job,
        'form': form,
        'comments': comments,
        'nbar': 'job_listings'
    }
    return render(request, 'warhawks/job-details.html', context)


"""

------------------------
APARTMENT SECTION - apartment Home, Add apartments, Add apartments comment and details handling
------------------------
"""
#apartments homepage with all the apartments listings
def apartments(request):
    apartments = Apartment.objects.all()
    count_a = apartments.count()
    context = {
        'apartments': apartments,
        'count_a': count_a,
        'nbar': 'apartments'
    }
    return render(request, 'warhawks/apartments.html', context)

# add apartments 
@login_required
def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            apart = form.save(commit=False)
            apart.posted_by = request.user
            apart.save()
            return redirect("main:home")
    else:
        form = ApartmentForm()
    return render(request, 'warhawks/add-apartments.html', {'form': form, 'nbar': 'apartments'})
    
# apartment_details
def apartment_details(request, slug):
    apartment = Apartment.objects.get(slug=slug)

    context = {
        'apartment': apartment,
        'nbar': 'apartments'
    }
    return render(request, 'warhawks/apartment-details.html', context)







"""
---------------------
STUDY MATERIALS - download and homepage of study materials
---------------------
"""
# study materials wit download?
def study_materials(request):
    sm = StudyMaterial.objects.all()

    context = {
        'sm': sm,
        'nbar': 'study_materials'
    }
    return render(request, 'warhawks/studymaterials.html', context)

# download study materials
@login_required
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


# add study materials
def add_study_materials(request):
    if request.user.is_authenticated:
        # permission granted
        if request.method == 'POST':
            form = AddStudyForm(request.POST,  request.FILES)
            if form.is_valid():
                file = form.save(commit=False)
                file.posted_by = request.user
                file.save()
                return redirect("main:study_materials")
        else:
            form = AddStudyForm()
            return render(request, 'warhawks/uploadfile.html', {'form': form})
    else:
        return redirect("main:home")






"""
LOST AND FOUND SECITON
HOMEPAGE, DETAILS AND COMMENTS WITH EMAIL OR PHONE LOGIC WITH MESSAGE HANDLING
"""
def lost_and_found(request):
    # get category
    cat = LFCategory.objects.all()

    # specify
    lf = LostAndFound.objects.all()
    lost_items = LostAndFound.objects.filter(category=cat[0])
    found_items = LostAndFound.objects.filter(category=cat[1])

    # resolved cases
    resolved = LostAndFound.objects.filter(resolved=True)

    context= {
        'lf': lf,
        'lost_items': lost_items,
        'found_items': found_items,
        'resolved': resolved,
        'nbar': 'lost_and_found'
    }
    return render(request, 'warhawks/lf.html', context)

