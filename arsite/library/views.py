from django.shortcuts import render

def browser(request):
    return render(request, 'library/browser.html')


def theatre(request):
    context = {
        'video':'https://www.youtube.com/watch?v=jwvXM1jnUUM&list=PLYBjZazfvgdPJWDG3_DMmk0Ge1UT0yMGS&index=161'
    }
    return render(request, 'library/theatre.html', context)