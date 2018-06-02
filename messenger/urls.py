from django.conf.urls import url
from . import views

app_name = 'messenger'

urlpatterns = [
    url(r'^messages/$', views.message_home, name='message_home'),
    
]
