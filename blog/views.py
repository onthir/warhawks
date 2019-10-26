from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    blogs_all = Blog.objects.all().order_by('-posted_on')
    page = request.GET.get('page', 1)

    paginator = Paginator(blogs_all, 10)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blogs': blogs,
        'nbar': 'blog'
    }
    return render(request, 'blog/bloghome.html', context)

# add blog
@login_required
def add_blog(request):
    if request.method == 'POST':
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            # save the other details
            blog.posted_by = request.user
            blog.save()
            return redirect("blog:home")
    else:
        form = AddBlogForm()
    return render(request, 'blog/add-blog.html', {'form': form,})

# blog details
def details(request,id, slug):
    blog = Blog.objects.get(id=id, slug=slug)
    context = {
        'post': blog
    }
    return render(request, 'blog/details.html', context)