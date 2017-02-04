from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    posted_by=models.CharField(max_length=20)
    email=models.EmailField()
    date=models.DateField()
    department=models.CharField(max_length=20)
    data=models.CharField(max_length=140)
    validity=models.BooleanField(default=True)
    resolved=models.BooleanField(default=False)
    cid=models.CharField(max_length=100,null=True)

    def __str__(self):
          return self.posted_by


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile') #1 to 1 link with Django User
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()
