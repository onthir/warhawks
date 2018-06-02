from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(job_category)
admin.site.register(Job)
admin.site.register(JobComment)
admin.site.register(a_type)
admin.site.register(Apartment)
admin.site.register(ApartmentComment)
admin.site.register(M_type)
admin.site.register(StudyMaterial)
admin.site.register(LFCategory)
admin.site.register(LostAndFound)