from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^add-blog/$', views.add_blog, name='add_blog'),
    url(r'^details/(?P<id>\d+)/(?P<slug>.*)/$', views.details, name='details')
]
