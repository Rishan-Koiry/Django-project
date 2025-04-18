from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Home Page!")


def geekyshows(request):
    return HttpResponse("Welcome to the GeekyShows Page!")
