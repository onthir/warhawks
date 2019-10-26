from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.accounts_home, name='home'),
    url(r'^register/$', views.register_account, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^complete-profile/$', views.complete_profile, name='complete_profile'),
    url(r'^edit-profile/$', views.edit_profile, name='edit_profile'),
    url(r'^display-profile/(?P<user>.*)/$', views.display_profile, name='display_profile')
]
