from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView  # Add this import

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", RedirectView.as_view(url="dashboard/", permanent=True)
    ),  # Redirect root to dashboard
    path("", include("users.urls")),  # Include your users app URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
