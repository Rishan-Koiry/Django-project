from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User


from .forms import UserRegisterForm, UserLoginForm
from .models import Profile
from django.shortcuts import render


def login_view(request):
    """Handle user login with proper form validation and security checks."""
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me", False)

            # Check if user exists before authentication
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, f'User "{username}" does not exist')
                return render(request, "users/login.html", {"form": form})

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Set session expiry based on remember_me
                if not remember_me:
                    request.session.set_expiry(0)  # Expire when browser closes
                else:
                    # Keep logged in for 2 weeks (in seconds)
                    request.session.set_expiry(60 * 60 * 24 * 14)

                # Check for next parameter for redirect after login
                next_url = request.GET.get("next")
                if next_url:
                    return redirect(next_url)
                return redirect("dashboard")
            else:
                messages.error(request, "Password is incorrect. Please try again.")
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", {"form": form})


# In your users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
@require_http_methods(["POST"])
def update_profile_picture(request):
    """Handle profile picture updates with validation."""
    if not request.FILES.get("profile_picture"):
        messages.error(request, "No profile picture uploaded.")
        return redirect("dashboard")

    try:
        profile, created = Profile.objects.get_or_create(user=request.user)

        # Check file size and type before saving
        image = request.FILES["profile_picture"]
        if image.size > 5 * 1024 * 1024:  # 5MB limit
            messages.error(request, "Profile picture must be less than 5MB.")
            return redirect("dashboard")

        allowed_types = ["image/jpeg", "image/png", "image/gif"]
        if image.content_type not in allowed_types:
            messages.error(request, "Only JPEG, PNG, and GIF images are allowed.")
            return redirect("dashboard")

        profile.profile_picture = image
        profile.save()

        messages.success(request, "Profile picture updated successfully!")
    except Exception as e:
        messages.error(request, f"Error updating profile picture: {str(e)}")

    return redirect("dashboard")


@login_required
def profile_settings(request):
    """View for user to edit their profile settings."""
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile.objects.create(user=request.user)

    # Add your profile form handling here

    context = {
        "profile": profile,
    }

    return render(request, "users/profile_settings.html", context)


@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")
