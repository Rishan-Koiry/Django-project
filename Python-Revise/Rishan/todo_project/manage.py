import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
application = get_wsgi_application()

# Project structure
# todo_project/
# ├── manage.py
# ├── todo_app/
# │   ├── migrations/
# │   ├── templates/
# │   │   └── todo_app/
# │   │       └── index.html
# │   ├── __init__.py
# │   ├── admin.py
# │   ├── apps.py
# │   ├── models.py
# │   ├── views.py
# │   ├── forms.py
# │   ├── tests.py
# │   └── urls.py
# └── db.sqlite3

# Ensure the Django project and app are created before modifying files
if not os.path.exists('todo_project'):
    os.system('django-admin startproject todo_project')
os.chdir('todo_project')
if not os.path.exists('todo_app'):
    os.system('python manage.py startapp todo_app')

# Updating settings.py
settings_path = 'todo_project/settings.py'
with open(settings_path, 'r') as file:
    content = file.read()

if "todo_app" not in content:
    with open(settings_path, 'a') as file:
        file.write("\nINSTALLED_APPS += ['todo_app']\n")

# Ensure migrations folder exists
migrations_folder = 'todo_app/migrations'
if not os.path.exists(migrations_folder):
    os.makedirs(migrations_folder)

# Defining the Task model
models_path = 'todo_app/models.py'
with open(models_path, 'w') as file:
    file.write('''
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
''')

# Creating the form
forms_path = 'todo_app/forms.py'
with open(forms_path, 'w') as file:
    file.write('''
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']
''')

# Creating views
views_path = 'todo_app/views.py'
with open(views_path, 'w') as file:
    file.write('''
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'todo_app/index.html', {'tasks': tasks, 'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')
''')

# Creating the URL patterns
urls_path = 'todo_app/urls.py'
with open(urls_path, 'w') as file:
    file.write('''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
''')

# Updating the project's urls.py
project_urls_path = 'todo_project/urls.py'
with open(project_urls_path, 'w') as file:
    file.write('''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
]
''')

# Ensure templates folder exists
templates_folder = 'todo_app/templates/todo_app'
if not os.path.exists(templates_folder):
    os.makedirs(templates_folder)

# Creating the HTML template
index_html_path = 'todo_app/templates/todo_app/index.html'
with open(index_html_path, 'w') as file:
    file.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Add Task</button>
    </form>
    <ul>
        {% for task in tasks %}
            <li>{{ task.title }} - {% if task.completed %}Completed{% else %}Not Completed{% endif %}
                <a href="{% url 'delete_task' task.id %}">Delete</a></li>
        {% endfor %}
    </ul>
</body>
</html>
''')

# Run migrations
os.system('python manage.py migrate')

print("Django To-Do List application setup complete! Run with: python manage.py runserver")
