from django.db import models
from django.contrib.auth.models import User
from warhawks.models import *
# Create your models here.
class UserMessage(models.Model):
    m_from = models.ForeignKey(User, related_name='message_from', on_delete=models.CASCADE)
    m_to   = models.ForeignKey(User, related_name='message_to', on_delete=models.CASCADE)
    post   = models.ForeignKey(LostAndFound, on_delete=models.CASCADE)
    date   = models.DateTimeField(auto_now_add=True)
    text   = models.TextField(max_length=500)
    seen   = models.BooleanField(default=False)

    def __str__(self):
        return self.text
