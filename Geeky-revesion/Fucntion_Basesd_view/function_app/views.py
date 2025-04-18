from django.shortcuts import render
from .models import User

def home(request):
    # Get the user's name from session if available
    user_name = request.session.get("user_name", None)
    error_message = None
    
    # Check if there's a user name in the session and if it exists in the database (not deleted)
    if user_name:
        existing_user = User.objects.filter(name=user_name, deleted=False).first()
        if not existing_user:
            # If user exists in session but not in database, remove from session
            user_name = None
            request.session.pop("user_name", None)

    if request.method == "POST":
        action = request.POST.get("action")

        # Handle name submission
        if action == "submit":
            submitted_name = request.POST.get("name")
            if submitted_name:
                # Check if user already has a name in session
                if user_name:
                    # If user already has a name, show error message requiring deletion first
                    error_message = "You already have a name submitted. Delete your current name before submitting a new one."
                    # Add a flag to show the error
                    request.session["show_error"] = True
                else:
                    # Check if the name exists in database
                    existing_user = User.objects.filter(name=submitted_name, deleted=False).first()
                    if not existing_user:
                        # Create new user if name doesn't exist
                        User.objects.create(name=submitted_name)
                    
                    # Store the name in session
                    user_name = submitted_name
                    request.session["user_name"] = user_name

        # Handle name deletion
        elif action == "delete":
            deleted_name = request.POST.get("name")
            if deleted_name and deleted_name == user_name:
                # Mark the user's name as deleted in the database
                existing_user = User.objects.filter(name=deleted_name, deleted=False).first()
                if existing_user:
                    existing_user.deleted = True
                    existing_user.save()
                
                # Remove from session
                user_name = None
                request.session.pop("user_name", None)
        
        # Handle admin deleting all names
        elif action == "delete_all" and request.user.is_staff:
            # Mark all users as deleted
            User.objects.update(deleted=True)
            
            # Clear the session
            user_name = None
            request.session.pop("user_name", None)

    # Get all non-deleted users for admin view
    all_users = None
    if request.user.is_staff:
        all_users = User.objects.filter(deleted=False)

    return render(
        request, 
        "function_app/home.html", 
        {
            "user_name": user_name,
            "all_users": all_users,
            "user_is_admin": request.user.is_staff,
            "error_message": error_message  # Send error message to template
        }
    )