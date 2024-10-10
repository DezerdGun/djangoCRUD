from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm, CombinedForm


def create_book_and_author(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            author = Author.objects.create(
                name=form.cleaned_data['author_name'],
                email=form.cleaned_data['author_email']
            )
            Book.objects.create(
                title=form.cleaned_data['book_title'],
                author=author,
                published_date=form.cleaned_data['published_date']
            )
            return redirect('list_books')
    else:
        form = CombinedForm()
    
    return render(request, 'library/create_book_and_author.html', {'form': form})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'library/list_books.html', {'books': books})

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'library/update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    
    return render(request, 'library/delete_book.html', {'book': book})
