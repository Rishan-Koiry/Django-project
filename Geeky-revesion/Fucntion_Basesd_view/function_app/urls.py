from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_root"),  # Add this line for the root path
]
