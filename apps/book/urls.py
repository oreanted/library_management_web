from django.urls import path
from . import views
from .views import BookSearch, BookUpdateView

urlpatterns = [
    path('book_listing/', views.BookView.as_view(), name='listing'),
    path('add_book/', views.BookAdd.as_view(), name='add_book'),
    path('edit/<int:id>', BookUpdateView.edit_book, name='edit_book'),
    path('delete/<int:id>', BookUpdateView.delete_book, name='delete_book'),
    path('search/', BookSearch.Search, name='search')
]
