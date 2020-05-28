from django.shortcuts import render
from . models import Video



def home(request):
    return render(request, 'main/home.html')


def about(request):
    context = {
        'title': 'About'
    }

    return render(request, 'main/about.html', context)


def browser(request):
    context = {
        'title': 'Browser',
        'videos': Video.objects.all()
    }

    return render(request, 'main/browser.html', context)

