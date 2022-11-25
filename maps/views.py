from django.shortcuts import render

# Create your views here.


def map(request):
    locality = (request.GET.get('locality'))
    # coordinates =
    coordiantes = [(12, 23), (12, 25)]
    context = {
        "coordinates": coordiantes
    }
    return render(request, 'maps/map.html', context=context)


def index(request):
    return render(request, 'maps/index.html', {})
