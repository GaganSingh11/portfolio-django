from django.contrib import admin
from .models import Service, Technology, Project, Review

# Register your models here.
admin.site.register(Service)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(Review)