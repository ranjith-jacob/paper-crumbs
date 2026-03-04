from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("books/", views.book_index, name="books-index"),
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book-detail"),
    path("books/create/", views.BookCreate.as_view(), name="book-create"),
]