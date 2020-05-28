from django.shortcuts import render

def browser(request):
    return render(request, 'library/browser.html')
