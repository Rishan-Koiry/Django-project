# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from accounts.views import home  # Import the home view
from accounts import views  # Import the views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home, name='home'), 
    path('check-auth/', views.check_auth, name='check_auth'),
# Add this line to your URL patterns
]