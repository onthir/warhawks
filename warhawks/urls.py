from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^jobs/$', views.job_listings, name='job_listings'),
    url(r'^apartments/$', views.apartments, name='apartments'),
    url(r'^studymaterials/$', views.study_materials, name='study_materials'),
    url(r'^download/(?P<path>.*)/$', views.download, name='download'),
    url(r'^upload-study-materials/$', views.add_study_materials, name='add_study_materials'),
    url(r'^lost-and-found/$', views.lost_and_found, name='lost_and_found'),
    url(r'^add-jobs/$', views.add_jobs, name='add_jobs'),
    url(r'^job-details/(?P<slug>.*)/$', views.job_details, name='job_details'),
    url(r'^add-apartment/$', views.add_apartment, name='add_apartment'),
    url(r'^apartments/details/(?P<slug>.*)/$', views.apartment_details, name='apartment_details'),
]
