from __future__ import unicode_literals

from django.db import models

class Complaint(models.Model):
    posted_by=models.CharField(max_length=20)
    email=models.EmailField()
    date=models.DateField()
    department=models.CharField(max_length=20)
    data=models.CharField(max_length=140)
    validity=models.BooleanField(default=True)
    resolved=models.BooleanField(default=False)

    def __str__(self):
          return self.posted_by

