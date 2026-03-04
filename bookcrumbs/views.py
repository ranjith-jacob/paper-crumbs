from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .models import Book

# Create your views here.
# def home(request):
#     return render(request, "index.html")

class Home(LoginView):
    template_name = "index.html"

# def book_index(request):
#     books = Book.objects.all()
#     return render(request, "books/book_list.html", {"books": books})

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = "__all__"

class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("book-list")