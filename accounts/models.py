from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    dob = models.DateField()
    address = models.CharField(max_length=300)
    cwid = models.IntegerField()
    class_of = models.IntegerField()
    gender = models.CharField(choices=CHOICES, max_length=6)
    profile_picture = models.ImageField(null=True, blank=True)
    scanned_id = models.FileField()
    started = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name