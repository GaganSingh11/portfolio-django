from django.contrib import admin
from .models import Service, Technology, Project

# Register your models here.
admin.site.register(Service)
admin.site.register(Technology)
admin.site.register(Project)