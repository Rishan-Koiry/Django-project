from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserInfoForm
from .models import UserInfo
import logging

# Set up logging
logger = logging.getLogger(__name__)

def home(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        logger.info(f"Form data received: {request.POST}")
        
        if form.is_valid():
            logger.info("Form is valid")
            roll = form.cleaned_data.get('roll')
            class_name = form.cleaned_data.get('class_name')
            phone = form.cleaned_data.get('phone')
            
            # Log the data we're checking
            logger.info(f"Checking for existing user with roll={roll}, class_name={class_name}, phone={phone}")
            
            # Check if a user with the same roll, class_name, and phone already exists
            existing_user = UserInfo.objects.filter(roll=roll, class_name=class_name, phone=phone).first()
            
            if existing_user:
                logger.info(f"Existing user found: {existing_user.name}")
                messages.warning(
                    request,
                    f"A user with roll number {roll}, class_name {class_name}, and phone {phone} already exists. "
                    f"Details: Name - {existing_user.name}, Roll - {existing_user.roll}, Class Name - {existing_user.class_name}, Phone - {existing_user.phone}."
                )
            else:
                logger.info("No existing user found, attempting to save")
                try:
                    user = form.save()
                    logger.info(f"User saved successfully with ID: {user.id}")
                    messages.success(request, "Your information has been submitted successfully! With RK School")
                    return redirect("home")
                except Exception as e:
                    logger.error(f"Error saving form: {str(e)}")
                    messages.error(request, f"Database error: {str(e)}")
        else:
            logger.error(f"Form errors: {form.errors}")
            messages.error(request, "There was an error in your submission. Please check the form.")
    else:
        form = UserInfoForm()
    return render(request, "homepage/home.html", {"form": form})
