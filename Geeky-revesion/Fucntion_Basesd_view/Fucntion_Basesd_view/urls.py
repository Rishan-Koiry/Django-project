from django.contrib import admin
from django.urls import path, include
from function_app import views  # Import views from your app

urlpatterns = [
    path("RK/", admin.site.urls),
    path("", views.home, name="home"),
]
