from django.shortcuts import render, redirect
from .models import Publisher
from ..books_app.models import Book

# Create your views here.
def create_publisher(request):
    Publisher.objects.create(name = request.POST['name'])
    return redirect('books:index')

def add_book_to_publisher(request):
    print request.POST
    publisher = Publisher.objects.get(id = request.POST['publisher'])
    book = Book.objects.get(id = request.POST['book'])
    publisher.books.add(book)
    return redirect('books:index')
