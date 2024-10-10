from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        
class CombinedForm(forms.Form):
    author_name = forms.CharField(max_length=100, label="Author Name")
    author_email = forms.EmailField(label="Author Email")
    book_title = forms.CharField(max_length=200, label="Book Title")
    published_date = forms.DateField(widget=forms.SelectDateWidget(), label="Published Date")