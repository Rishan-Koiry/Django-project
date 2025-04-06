# accounts/urls.py

from django.urls import path
from .views import register, login_view, dashboard, logout_view  # Ensure all views are correctly imported
from .views import register, login_view, dashboard, logout_view, borrow_book

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('borrow-book/', borrow_book, name='borrow_book'),  # This URL name must match
# Ensure this line is present
]