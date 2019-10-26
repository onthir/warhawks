from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    
    url(r'^apartments/$', views.apartments, name='apartments'),
    url(r'^studymaterials/$', views.study_materials, name='study_materials'),
    url(r'^download/(?P<path>.*)/$', views.download, name='download'),
    url(r'^upload-study-materials/$', views.add_study_materials, name='add_study_materials'),
    url(r'^lost-and-found/$', views.lost_and_found, name='lost_and_found'),

    # URL PATTERNS FOR JOBS
    url(r'^jobs/$', views.job_listings, name='job_listings'),
    url(r'^add-jobs/$', views.add_jobs, name='add_jobs'),
    url(r'^job-details/(?P<slug>.*)/$', views.job_details, name='job_details'),
    url(r'^edit-job/(?P<slug>.*)/$', views.edit_job, name='edit_job'),
    url(r'^delete-job/(?P<slug>.*)/$', views.delete_job, name='delete_job'),

    url(r'^add-apartment/$', views.add_apartment, name='add_apartment'),
    url(r'^apartments/details/(?P<slug>.*)/$', views.apartment_details, name='apartment_details'),
    url(r'^edit-accomodation/(?P<slug>.*)/$', views.edit_apartment, name='edit_apartment'),


    # read notification
    url(r'^read-notification/(?P<id>\d+)/(?P<slug>.*)/$', views.read_job_notifiation, name='read_job_notifiation'),
    url(r'^read-apartment-notification/(?P<id>\d+)/(?P<slug>.*)/$', views.read_apartment_notifiation, name='read_apartment_notifiation'),
    url(r'^read-lostandfound-notification/(?P<id>\d+)/(?P<slug>.*)/$', views.read_lf_notifiation, name='read_lf_notifiation'),


    # lost and found
    url(r'^add-lost-and-found/$', views.add_lost_and_found, name='add_lost_and_found'),
    url(r'lostandfound/(?P<slug>.*)/$', views.lost_and_found_details, name='lost_and_found_details')
]
