# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard on successful login
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def check_auth(request):
    """Endpoint to check if a user is authenticated"""
    return JsonResponse({
        'authenticated': request.user.is_authenticated
    })

# Assuming you have a Book model or create a simple one
class Book:
    def __init__(self, id, title, author, cover_image=None):
        self.id = id
        self.title = title
        self.author = author
        self.cover_image = cover_image

# Mock database of books (replace with real database in production)
BOOKS = {
    "1": Book(1, "Python Programming", "John Smith", "python_book.jpg"),
    "2": Book(2, "Java Fundamentals", "Sarah Johnson", "java_book.jpg"),
    "3": Book(3, "JavaScript Essentials", "David Brown", "javascript_book.jpg"),
}

# Mock database for borrowed books (replace with real database in production)
BORROWED_BOOKS = {}  # user_id -> [book_objects]

@csrf_exempt
@require_POST
def borrow_book(request):
    """Handle the book borrowing functionality"""
    try:
        # Try to parse JSON data from request body
        try:
            data = json.loads(request.body)
            book_title = data.get('book_title')
            
            # Find book by title
            book = None
            for book_id, book_obj in BOOKS.items():
                if book_obj.title == book_title:
                    book = book_obj
                    break
                    
            if not book:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Book not found'
                })
                
            # Store the borrowed book in our mock database
            user_id = request.user.id
            if user_id not in BORROWED_BOOKS:
                BORROWED_BOOKS[user_id] = []
            
            # Set return date to 14 days from now
            return_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
            
            # Add book to user's borrowed books with borrow and return dates
            BORROWED_BOOKS[user_id].append({
                'book': book,
                'borrow_date': datetime.now().strftime('%Y-%m-%d'),
                'return_date': return_date
            })
            
            return JsonResponse({
                'status': 'success',
                'message': f'You have successfully borrowed "{book_title}"!'
            })
            
        # If JSON parsing fails, try form data
        except json.JSONDecodeError:
            book_id = request.POST.get('book_id')
            return_date = request.POST.get('return_date')
            
            if not book_id or not return_date:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Missing required information'
                })
            
            # Get the book from our mock database
            book = BOOKS.get(book_id)
            if not book:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Book not found'
                })
            
            # Store the borrowed book in our mock database
            user_id = request.user.id
            if user_id not in BORROWED_BOOKS:
                BORROWED_BOOKS[user_id] = []
            
            # Add book to user's borrowed books with borrow and return dates
            BORROWED_BOOKS[user_id].append({
                'book': book,
                'borrow_date': datetime.now().strftime('%Y-%m-%d'),
                'return_date': return_date
            })
            
            # Redirect to dashboard to show the borrowed book
            return redirect('dashboard')
            
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

@login_required
def dashboard(request):
    context = {
        'name': request.user.name,  # Using name instead of username
        'email': request.user.email,
        'today': datetime.now(),
        'available_books': BOOKS.values(),
    }
    
    # Add borrowed books to context if any
    user_id = request.user.id
    if user_id in BORROWED_BOOKS:
        context['borrowed_books'] = BORROWED_BOOKS[user_id]
    
    return render(request, 'accounts/dashboard.html', context)