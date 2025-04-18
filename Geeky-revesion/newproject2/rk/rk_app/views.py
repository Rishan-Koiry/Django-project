from django.shortcuts import render

# Removed unused import
# from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "rk_app/home.html")


def about(request):
    return render(request, "rk_app/about.html")
