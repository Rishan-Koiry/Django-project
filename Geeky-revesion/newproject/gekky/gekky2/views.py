from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Home Page 2!")


def geekyshows(request):
    return HttpResponse("Welcome to the GeekyShows Page! 2")
