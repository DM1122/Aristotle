"""Main app views."""

# django
from django.shortcuts import render

# from .models import Video


def home(request):
    """Home view."""
    return render(request, "main/home.html")


def about(request):
    """About page view."""
    context = {"title": "About"}

    return render(request, "main/about.html", context)


def tools(request):
    """Access to publically available tools page."""
    return render(request, "main/tools.html")


def vision(request):
    """Aristotle Digital's vision."""
    return render(request, "main/vision.html")


# def browser(request):
#     context = {
#         'title': 'Browser',
#         'videos': Video.objects.all()
#     }

#     return render(request, 'main/browser.html', context)
