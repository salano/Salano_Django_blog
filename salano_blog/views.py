from django.shortcuts import render
from django.http import HttpResponse


post = [
    {
        'author': 'SalanoCS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'September 14, 2024'
    },
    {
        'author': 'TanisTS',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'September 14, 2024'
    }
]


def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
