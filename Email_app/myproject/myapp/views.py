from django.shortcuts import render, redirect
from django.urls import path

def index(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        if item:
            # Add item to the session
            items = request.session.get('items', [])
            items.append(item)
            request.session['items'] = items
            return redirect('index')

    # Retrieve items from the session
    items = request.session.get('items', [])
    return render(request, 'index.html', {'items': items, 'user_name': 'User'})

def delete_item(request, item_index):
    if request.method == 'POST':
        # Retrieve items from the session
        items = request.session.get('items', [])
        if 0 <= item_index < len(items):
            # Remove the item at the specified index
            items.pop(item_index)
            request.session['items'] = items
    return redirect('index')