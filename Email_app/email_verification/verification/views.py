import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import EmailForm, CodeForm
from .models import Verification


def home(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            code = "".join(random.choices("0123456789", k=6))  # Generate a 6-digit code
            Verification.objects.create(
                email=email, code=code
            )  # Save email and code to the database

            # Send the email with the verification code
            send_mail(
                "Your Verification Code",
                f"Your RK verification code is: {code}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return redirect("verify")  # Redirect to the verification page
    else:
        form = EmailForm()
    return render(request, "home.html", {"form": form})


def verify(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                verification = Verification.objects.get(
                    code=code
                )  # Check if the code exists
                verification.is_verified = True
                verification.save()
                return render(
                    request, "success.html"
                )  # Code matched, show success page
            except Verification.DoesNotExist:
                return render(
                    request,
                    "verify.html",
                    {"form": form, "error": "Invalid Please Enter The Right code"},
                )  # Code did not match
    else:
        form = CodeForm()
    return render(request, "verify.html", {"form": form})


def success(request):
    return render(request, "success.html")
