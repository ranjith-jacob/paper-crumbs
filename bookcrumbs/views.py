from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

# Create your views here.
def home(request):
    return render(request, "index.html")

# def book_index(request):
#     books = Book.objects.all()
#     return render(request, "books/book_list.html", {"books": books})

class BookList(ListView):
    model = Book