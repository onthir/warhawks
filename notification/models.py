from django.db import models
from warhawks.models import *
from django.contrib.auth.models import User

# table for notificaiton in job_listings
class N_job(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    post = models.ForeignKey(JobComment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

# table for notificaiton in apartments
class N_apartment(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    post = models.ForeignKey(ApartmentComment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='from_user_apartment', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user_apartment', on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

# table for notificaiton in lost and found
class N_lostandfound(models.Model):
    lf = models.ForeignKey(LostAndFound, on_delete=models.CASCADE)
    post = models.ForeignKey(LFComment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='from_user_lost', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user_lost', on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message