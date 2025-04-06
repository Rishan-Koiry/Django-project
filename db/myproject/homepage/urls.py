from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="RK"),
    path("RK", views.home, name="RK"),

    
]
