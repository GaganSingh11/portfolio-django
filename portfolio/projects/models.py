from unicodedata import category
from django.db import models

import uuid

# Create your models here.
class Service(models.Model):
    service_title = models.CharField(max_length=200)
    service_description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.service_title


class Technology(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Project(models.Model):
    CATEGORIES = [
        ('WEB APPS', 'WEB APPS '),
        ('APIS', 'APIS '),
        ('STATIC SITE', 'STATIC SITE'),
    ]
    
    id = models.BigAutoField(primary_key=True)
    project_thumbnail = models.ImageField(null=True, blank=True, default="default_thumbnail.jpg")
    project_image = models.ImageField(null=True, blank=True, default="default_project.jpg")
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    categories = models.CharField(max_length=100, choices=CATEGORIES)
    date = models.DateField()
    technologies = models.ManyToManyField(Technology, blank=True)
    project_link = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title

    
