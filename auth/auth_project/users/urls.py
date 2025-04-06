from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url='dashboard/'), name="home"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("/home", RedirectView.as_view(url='dashboard/'), name="home_alias"),  # Fixed this line
    path("update-profile-picture/", views.update_profile_picture, name="update_profile_picture"),
]
