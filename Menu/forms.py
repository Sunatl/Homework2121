# forms.py
from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ('book',)