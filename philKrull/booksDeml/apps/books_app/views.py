from django.shortcuts import render, redirect
from .models import Book, Author
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'all_authors': Author.objects.all(),
        'all_books': Book.objects.all()
    }
    return render(request, 'books_app/index.html', context)

def create_author(request):
    response = Author.objects.add_author(request.POST)
    if not response['status']:
        for error in response['errors']:
            messages.error(request, error)
    # Author.objects.create(name = request.POST['name'])
    return redirect('/')

def create_book(request):
    author = Author.objects.get(id = request.POST['author'])
    Book.objects.create(title = request.POST['title'], author = author)
    return redirect('/')
