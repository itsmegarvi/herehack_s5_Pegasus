from django.shortcuts import render

# Create your views here.


def map(request):
    return render(request, 'maps/map.html', {})


def index(request):
    return render(request, 'maps/index.html', {})
