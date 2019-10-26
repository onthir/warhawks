from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime

class job_category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Job(models.Model):
    j_type = models.ForeignKey(job_category, on_delete=models.CASCADE)
    company = models.CharField(max_length=500)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    position = models.CharField(max_length=500)
    description = models.TextField(max_length=1500)
    slug = models.SlugField(max_length=500, default=None)
    salary = models.FloatField()
    hits = models.IntegerField()


    def __str__(self):
        return self.company

    def _get_unique_slug(self):
        slug = slugify(self.company)
        unique_slug = slug
        num = 1
        while Job.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    
    @property
    def date(self):
          return self.posted_on

    # get class name for DLT
    def get_cname(self):
        class_name = 'Job'
        return class_name 
# comments on job
class JobComment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    edit = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.job.company

# apartment type 
class a_type(models.Model):
    apartment_type = models.CharField(max_length=50)

    def __str__(self):
        return self.apartment_type

# apartments
class Apartment(models.Model):
    posted_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    edit = models.DateTimeField(auto_now=True)
    a_type = models.ForeignKey(a_type, on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    distance_from_university = models.FloatField()
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    picture = models.ImageField(blank=True, null=True)
    slug = models.SlugField(max_length=500, default=None)
    def __str__(self):
        return self.location 

    def _get_unique_slug(self):
        slug = slugify(self.location)
        unique_slug = slug
        num = 1
        while Apartment.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    # get class name for DLT
    def get_cname(self):
        class_name = 'Apartment'
        return class_name 
# comments on apartment
class ApartmentComment(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    edit = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.apartment.location

class M_type(models.Model):
    mt = models.CharField(max_length=500)

    def __str__(self):
        return self.mt

class StudyMaterial(models.Model):
    study_material_type  = models.ForeignKey(M_type, on_delete=models.CASCADE)
    title                = models.CharField(max_length=100)
    posted_by            = models.ForeignKey(User,on_delete=models.CASCADE)
    description          = models.TextField(max_length=1000, null=True, blank=True)
    date                 = models.DateTimeField(auto_now_add=True)
    file_content         = models.FileField()
    downloads            = models.IntegerField(default=0)
    preview_picture      = models.ImageField(default=None, null=True, blank=True)
    def __str__(self):
        return self.title



# lost and found
class  LFCategory(models.Model):
    lftype = models.CharField(max_length=150)

    def __str__(self):
        return self.lftype


class LostAndFound(models.Model):
    category = models.ForeignKey(LFCategory, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    found_or_lost_on = models.DateField(default=datetime.datetime.now())
    resolved = models.BooleanField(default=False)
    hits = models.IntegerField(default=0)
    slug = models.SlugField(max_length=500, default=None)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while LostAndFound.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

# comments on lost and found
class LFComment(models.Model):
    lf = models.ForeignKey(LostAndFound, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    edit = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.comment


# feedbacks
"""
FEEDBACKS FROM THE USERS GOES HERE
"""
class Feedback(models.Model):
    email = models.EmailField(max_length=250)
    full_name = models.CharField(max_length=250)
    feedback = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email