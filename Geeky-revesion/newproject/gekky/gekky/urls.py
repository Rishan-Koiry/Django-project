"""
URL configuration for gekky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from geekyshows import views
from gekky2 import views as views2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("geekyshows/", views.geekyshows, name="geekyshows"),
    path("home/", views2.home, name="home2"),
    path("home2/", views2.home, name="home2"),
]
