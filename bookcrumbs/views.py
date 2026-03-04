from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    # fields = "__all__"
    fields = ["image", "name", "author", "series", "genre", "published_year", "characters", "locations"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookUpdate(UpdateView):
    model = Book
    # fields = "__all__"
    fields = ["image", "name", "author", "series", "genre", "published_year", "characters", "locations"]

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("book-list")

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')
        else:
            error_message = "Invalid sign up, please try again!"
    form = UserCreationForm()
    context = {'form': form, "error_message": error_message}
    return render(request, "signup.html", context)