from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    posted_by=models.CharField(max_length=20)
    date=models.DateField()
    department=models.CharField(max_length=20, null=True, blank=True)
    data=models.CharField(max_length=140)
    validity=models.BooleanField(default=True)
    resolved=models.BooleanField(default=False)
    cid=models.CharField(max_length=100, null=True)

    def __str__(self):
          return self.posted_by


class Profile(models.Model):

    DEPARTMENT_CHOICES = (
        ('EDC', 'Education'),
        ('CSH', 'Cosha'),
        ('HST', 'Hostel'),
        ('GEN', 'General'),
    )
    user = models.OneToOneField(User, 
                        on_delete=models.CASCADE, 
                        related_name="user")
    approved = models.BooleanField(default=False)
    department = models.CharField(
                        max_length=3, 
                        choices=DEPARTMENT_CHOICES, 
                        default='GEN')

    def __str__(self):
        return self.user.username