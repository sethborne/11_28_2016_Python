from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.
def index(request):
    context = {
        'all_authors': Author.objects.all(),
        'all_books': Book.objects.all()
    }
    return render(request, 'books_app/index.html', context)

def create_author(request):
    Author.objects.create(name = request.POST['name'])
    return redirect('/')

def create_book(request):
    author = Author.objects.get(id = request.POST['author'])
    Book.objects.create(title = request.POST['title'], author = author)
    return redirect('/')
