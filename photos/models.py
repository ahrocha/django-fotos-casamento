from django.db import models

# Create your models here.

class Photo(models.Model):
    filename = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    taken_date = models.DateTimeField(blank=True, null=True)
    exif = models.TextField(blank=True, null=True)
    file = models.FileField(max_length=200, blank=True, null=True)
