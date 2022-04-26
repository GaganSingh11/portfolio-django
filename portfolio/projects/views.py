from django.shortcuts import render
from .models import Review, Service, Project, Technology
from .forms import ContactForm

# Create your views here.
def homePage(request):
    services = Service.objects.all()
    project = Project.objects.all()
    review = Review.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()

    context = {'services': services, 'projects': project, 'reviews': review, 'form':form}
    return render(request, 'projects/index.html', context)

