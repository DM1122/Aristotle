"""Views for library app."""

# django
from django.shortcuts import render


def browser(request):
    """Display browser page for video browsing."""
    return render(request, "library/browser.html")


def theatre(request):
    """Display theatre page for video streaming."""
    context = {"video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    return render(request, "library/theatre.html", context)
