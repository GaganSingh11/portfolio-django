from django.shortcuts import render
from .models import Service

# Create your views here.
def homePage(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'projects/index.html', context)