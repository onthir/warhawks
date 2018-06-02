from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.accounts_home, name='home'),
    url(r'^register/$', views.register_account, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^complete-profile/$', views.complete_profile, name='complete_profile'),
]
