from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    return render(request, "index.html")

def book_index(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})