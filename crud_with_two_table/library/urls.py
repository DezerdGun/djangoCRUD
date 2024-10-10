from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book_and_author, name='create_book_and_author'),
    path('', views.list_books, name='list_books'),
    path('update/<int:book_id>/', views.update_book, name='update_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]