from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import AddStudyForm, AddJobForm, JobCommentForm, ApartmentForm, ApartmentCommentForm, LostandFoundForm, LFCommentForm, EditJobForm, EditApartmentForm
from django.contrib.auth.decorators import login_required
from blog.models import *
from accounts.models import *
from notification.models import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain

""" THIS IS THE HOME PAGE WHERE TOP FOUR CHOICES OF JOBS, APARTMENTS AND BLOGS ARE DISPLAYED
ALSO SOME OTHER CONTENT ARE DISPLAYED

/* HOME */

"""

# get notification
def get_notification(user):
    if user.is_authenticated:
        # NOTIFICATION
        try:
            job_notifications = N_job.objects.filter(to_user=user, read=False).order_by('-date')
            job_count = job_notifications.count()
            # apartment notificaitons
            apartment_notifications = N_apartment.objects.filter(to_user=user, read=False).order_by('-date')
            apartment_count = apartment_notifications.count()

            # lost and found notifications
            lf_notifications = N_lostandfound.objects.filter(to_user=user, read=False).order_by('date')
            lf_count = lf_notifications.count()

            total_not_count = job_count + apartment_count + lf_count

            
        except:
            job_notifications = None
            job_count = None

            apartment_notifications = None
            apartment_count = None

            lf_notifications = None
            lf_count = None

            total_not_count = 0 
        return job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count
    else:
        job_notifications = None
        job_count = None

        apartment_notifications = None
        apartment_count = 0

        lf_notifications = None
        lf_count =  0

        total_not_count = 0
        return job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count

"""
HOME PAGE OF THE WEBSITE WHERE FEED IS DISPLAYED IF THE USER IS AUTHENTICATED ELSE
A GENERIC HOMEPAGE WITH SOME DETAILS IS DISPLAYED
"""
def home(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    # SEND FEEDBACK
    """ FEEDBACK FROM THE VISITORS """
    if request.method == 'POST':
        # get everything
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        msg = request.POST.get('msg')

        # create feedback object
        feedback = Feedback(
            email = email,
            full_name = full_name,
            feedback = msg
        )
        feedback.save()
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        profile = Profile.objects.get(user=user)

        # news feed on the homepage
        jobs = Job.objects.all().order_by('-posted_on')
        
        apartments = Apartment.objects.all().order_by('-date')
        
        blogs = Blog.objects.all().order_by('-posted_on')[:2]
        
        feed = (sorted(chain(jobs, apartments),
                 key=lambda instance: instance.date, reverse=True))

        # NOTIFICATION
        job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)        

        context = {
            'profile': profile,
            'jobs': jobs,
            'apartments': apartments,
            
            'job_notifications': job_notifications,
            'job_count': job_count,
            'apartment_notifications': apartment_notifications,
            'apartment_count' : apartment_count,
            'total_not_count': total_not_count,
            'lf_notifications': lf_notifications,
            'lf_count': lf_count,
            'notif_id': notif_id,

            'feed': feed,
            'blogs': blogs
        }
        
        return render(request, 'warhawks/uhome.html', context)
    else:
        return render(request, 'warhawks/index.html')

"""

------------------------
JOB SECTION - Job Home, Add Jobs, Add job comment and details handling
------------------------
"""
# jobs home page with all the job listings
def job_listings(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    jobs = Job.objects.all().order_by('-posted_on')
    count_job = jobs.count()

    # pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(jobs, 10)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    context = {
        'jobs': jobs,
        'count_job': count_job,
        'nbar': 'job_listings',

        'job_notifications': job_notifications,
        'job_count': job_count,
        'apartment_notifications': apartment_notifications,
        'apartment_count' : apartment_count,
        'total_not_count': total_not_count,
        'lf_notifications': lf_notifications,
        'lf_count': lf_count,

        'notif_id': notif_id
    }
    return render(request, 'warhawks/jobs.html', context)

# add jobs
@login_required
def add_jobs(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    types = job_category.objects.all()
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
    return render(request, 'warhawks/addjob.html', {'form': form,
                                                    'nbar': 'job_listings',
                                                    'types':types,

                                                    'job_notifications': job_notifications,
                                                    'job_count': job_count,
                                                    'apartment_notifications': apartment_notifications,
                                                    'apartment_count' : apartment_count,
                                                    'total_not_count': total_not_count,
                                                    'lf_notifications': lf_notifications,
                                                    'lf_count': lf_count,
                                                    
                                                    'notif_id': notif_id,
                                                    'action': 'Add'})
# JOB DETAILS
def job_details(request, slug):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')
    # job notifications
    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    job = Job.objects.get(slug=slug)
    rest_jobs = Job.objects.all().exclude(slug=job.slug)
    comments = JobComment.objects.all().order_by('-date').filter(job=job)
    
    # comment form
    if request.method == 'POST':
        form = JobCommentForm(request.POST or None)
        if form.is_valid():
            com = form.save(commit=False)
            com.job = job
            try:
                com.user = request.user
                com.save()
                # send notification
                notification = N_job(
                    job = job,
                    post = com,
                    from_user = request.user,
                    to_user = job.posted_by,
                    message = str(request.user) + " has commented on your job listing."

                )
                notification.save()
                return HttpResponseRedirect('/job-details/%s/' %slug)
            except:
                return redirect("accounts:login")
    else:
        form = JobCommentForm()

    context = {
        'job': job,
        'form': form,
        'comments': comments,
        'nbar': 'job_listings',
        'rest_jobs': rest_jobs,

        'job_notifications': job_notifications,
        'job_count': job_count,
        'apartment_notifications': apartment_notifications,
        'apartment_count' : apartment_count,
        'total_not_count': total_not_count,
        'lf_notifications': lf_notifications,
        'lf_count': lf_count,

        'notif_id': notif_id,
        
    }
    return render(request, 'warhawks/job-details.html', context)
# EDIT JOB
def edit_job(request, slug):
    # get the instance of job
    job = Job.objects.get(slug=slug)
    if request.user.is_authenticated:
        if request.user == job.posted_by:
            # grant permission to edit
            if request.method == 'POST':
                form  = EditJobForm(request.POST, instance=job)
                if form.is_valid():
                    print("Valid Form")
                    form.save()
                    return HttpResponseRedirect('/job-details/%s/' %slug)
            else:
                form = EditJobForm(instance=job)
            return render(request, 'warhawks/addjob.html', {'form': form, 'action': 'Edit'})
        else:
            return redirect("main:job_listings")
    else:
        return redirect("main:job_listings")
# DELETE JOB 
# DELETE JOB INSTANCE
def delete_job(request, slug):
    # get job
    job = Job.objects.get(slug=slug)
    if request.user.is_authenticated:
        if request.user == job.posted_by:
            # grant permission
            job.delete()
            return redirect("main:job_listings")
        else:
            return redirect("main:job_listings")
    else:
        return redirect("main:job_listings")

"""

------------------------
APARTMENT SECTION - apartment Home, Add apartments, Add apartments comment and details handling
------------------------
"""
#apartments homepage with all the apartments listings
def apartments(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    apartments = Apartment.objects.all().order_by('-date')
    count_a = apartments.count()
    context = {
        'apartments': apartments,
        'count_a': count_a,
        'nbar': 'apartments',

        'job_notifications': job_notifications,
        'job_count': job_count,
        'apartment_notifications': apartment_notifications,
        'apartment_count' : apartment_count,
        'total_not_count': total_not_count,
        'lf_notifications': lf_notifications,
        'lf_count': lf_count,
        
        'notif_id': notif_id
    }
    return render(request, 'warhawks/apartments.html', context)

# add apartments 
@login_required
def add_apartment(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            apart = form.save(commit=False)
            apart.posted_by = request.user
            apart.save()
            return redirect("main:home")
    else:
        form = ApartmentForm()
    return render(request, 'warhawks/add-apartments.html', {'form': form, 'nbar': 'apartments',
                                                                    'job_notifications': job_notifications,
                                                                    'job_count': job_count,
                                                                    'apartment_notifications': apartment_notifications,
                                                                    'apartment_count' : apartment_count,
                                                                    'total_not_count': total_not_count,
                                                                    'lf_notifications': lf_notifications,
                                                                    'lf_count': lf_count,
                                                                    
                                                                    'notif_id': notif_id,
                                                                    'action' :'Add Accomodation'})
    
# apartment_details
def apartment_details(request, slug):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    apartment = Apartment.objects.get(slug=slug)
    comments = ApartmentComment.objects.filter(apartment=apartment).order_by('-date')
    # add comment on the apartment
    if request.method == 'POST':
        form = ApartmentCommentForm(request.POST or None)
        if form.is_valid():
            com = form.save(commit=False)
            com.apartment = apartment
            try:
                com.user = request.user
                com.save()

                # notificaiton
                notification = N_apartment(
                    apartment = apartment,
                    post = com,
                    from_user = request.user,
                    to_user = apartment.posted_by,
                    message = str(request.user) + " has commented on your apartment listing."

                )
                notification.save()
                return HttpResponseRedirect('/apartments/details/%s/' %slug)
            except:
                return redirect("accounts:login")
    else:
        form = ApartmentCommentForm()
    context = {
        'apartment': apartment,
        'nbar': 'apartments',
        'form': form,
        'comments': comments,

        'job_notifications': job_notifications,
        'job_count': job_count,
        'apartment_notifications': apartment_notifications,
        'apartment_count' : apartment_count,
        'total_not_count': total_not_count,
        'lf_notifications': lf_notifications,
        'lf_count': lf_count,

        'notif_id': notif_id
    }
    return render(request, 'warhawks/apartment-details.html', context)

# EDIT APARTMENT
def edit_apartment(request, slug):
    # get apartment
    apartment  = Apartment.objects.get(slug=slug)
    if request.user.is_authenticated:
        if request.user == apartment.posted_by:
            # grant permission
            if request.method == 'POST':
                form = EditApartmentForm(request.POST,request.FILES, instance=apartment)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/apartments/details/%s/' %slug)
            else:
                form = EditApartmentForm(instance=apartment)
            return render(request, 'warhawks/add-apartments.html', {'form': form, 'action':'Edit Accomodation'})
        else:
            return redirect("main:apartments")
    else:
        return redirect("main:apartments")







"""
---------------------
STUDY MATERIALS - download and homepage of study materials
---------------------
"""
# study materials wit download?
def study_materials(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    sm = StudyMaterial.objects.all()

    context = {
        'sm': sm,
        'nbar': 'study_materials',

        'job_notifications': job_notifications,
        'job_count': job_count,
        'apartment_notifications': apartment_notifications,
        'apartment_count' : apartment_count,
        'total_not_count': total_not_count,
        'lf_notifications': lf_notifications,
        'lf_count': lf_count,

        'notif_id': notif_id
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
@login_required
def add_study_materials(request):
    notif_id = request.GET.get('notif')
    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
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
            return render(request, 'warhawks/uploadfile.html', {'form': form,
                                                        'job_notifications': job_notifications,
                                                        'job_count': job_count,
                                                        'apartment_notifications': apartment_notifications,
                                                        'apartment_count' : apartment_count,
                                                        'total_not_count': total_not_count,
                                                        'lf_notifications': lf_notifications,
                                                        'lf_count': lf_count,
                                                        'notif_id': notif_id})
    else:
        return redirect("main:home")


"""
LOST AND FOUND SECITON
HOMEPAGE, DETAILS AND COMMENTS WITH EMAIL OR PHONE LOGIC WITH MESSAGE HANDLING
"""
def lost_and_found(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    # get category
    cat = LFCategory.objects.all()

    # specify
    lf = LostAndFound.objects.all()
    lost_items = LostAndFound.objects.filter(category=cat[0]).order_by('-posted_on')
    found_items = LostAndFound.objects.filter(category=cat[1]).order_by('-posted_on')
    # resolved cases
    resolved = LostAndFound.objects.filter(resolved=True)

    context= {
        'lf': lf,
        'lost_items': lost_items,
        'found_items': found_items,
        'resolved': resolved,
        'nbar': 'lost_and_found',

        'job_notifications': job_notifications,
        'job_count': job_count,
        'apartment_notifications': apartment_notifications,
        'apartment_count' : apartment_count,
        'total_not_count': total_not_count,
        'lf_notifications': lf_notifications,
        'lf_count': lf_count,

        'notif_id': notif_id
    }
    return render(request, 'warhawks/lf.html', context)

@login_required
def add_lost_and_found(request):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    if request.method == 'POST':
        form = LostandFoundForm(request.POST, request.FILES)
        if form.is_valid():
            lf = form.save(commit=False)
            
            # posted by
            lf.posted_by = request.user
            lf.save()
            return HttpResponseRedirect('/lost-and-found/')
    else:
        form = LostandFoundForm()
    return render(request, 'warhawks/add-lost-and-found.html', {'form': form, 'notif_id': notif_id})

# lost and found details
def lost_and_found_details(request,slug):
    # notif id to show the recent id
    notif_id = request.GET.get('notif')

    job_notifications, job_count, apartment_notifications, apartment_count, lf_notifications, lf_count, total_not_count = get_notification(request.user)
    lf = LostAndFound.objects.get(slug=slug)
    comments =LFComment.objects.all().order_by('-date')
    # comment
    if request.method == 'POST':
        form = LFCommentForm(request.POST or None)
        if form.is_valid():
            com = form.save(commit=False)
            com.lf = lf
            try:
                com.user = request.user
                com.save()

                # notificaiton
                notification = N_lostandfound(
                    lf = lf,
                    post = com,
                    from_user = request.user,
                    to_user = lf.posted_by,
                    message = str(request.user) + " has commented on your lost and found report."

                )
                notification.save()
                return HttpResponseRedirect('/lostandfound/%s/' %slug)
            except:
                return redirect("accounts:login")
    else:
        form = LFCommentForm()
    context = {
        'lf': lf,
        'form': form,
        'comments': comments,

        'job_notifications': job_notifications,
        'job_count': job_count,
        'apartment_notifications': apartment_notifications,
        'apartment_count' : apartment_count,
        'total_not_count': total_not_count,
        'lf_notifications': lf_notifications,
        'lf_count': lf_count,

        'notif_id': notif_id
    }
    return render(request, 'warhawks/lfdetails.html', context)
"""
READ NOTIFICATIONS FUNCTIONS
"""
def read_job_notifiation(request, id, slug):
    job = Job.objects.get(slug=slug)
    notf = N_job.objects.get(id=id, job=job)
    if notf.read == False:
        notf.read = True
        notf.save()
    return HttpResponseRedirect('/job-details/%s/?notif=%d' %(slug, notf.post.id))
# read apartment notifications
def read_apartment_notifiation(request, id, slug):
    apartment = Apartment.objects.get(slug=slug)
    notf = N_apartment.objects.get(id=id, apartment=apartment)
    if notf.read == False:
        notf.read = True
        notf.save()
    return HttpResponseRedirect('/apartments/details/%s/?notif=%d' %(slug, notf.post.id))
# read lost&found notifications
def read_lf_notifiation(request, id, slug):
    lf = LostAndFound.objects.get(slug=slug)
    notf = N_lostandfound.objects.get(id=id, lf=lf)
    if notf.read == False:
        notf.read = True
        notf.save()
    return HttpResponseRedirect('/lostandfound/%s/?notif=%d' %(slug, notf.post.id))