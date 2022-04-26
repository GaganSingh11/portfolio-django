from django.shortcuts import render
from .models import Review, Service, Project, Technology

# Create your views here.
def homePage(request):
    services = Service.objects.all()
    project = Project.objects.all()
    review = Review.objects.all()
    context = {'services': services, 'projects': project, 'reviews': review}
    return render(request, 'projects/index.html', context)