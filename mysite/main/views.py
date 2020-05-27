from django.shortcuts import render


posts = [
    {
        'author':'David',
        'title':'A post',
        'content':'Hellow world!',
        'date':'august 27, 2019'
    },
    {
        'author':'Bruck',
        'title':'A post',
        'content':'Hellow world2!',
        'date':'Jan 22, 2029'
    }

]



def home(request):
    context = {
        'posts':posts
    }

    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'title':'About'
    }
    return render(request, 'main/about.html', context)
