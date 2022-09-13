from django import forms
from .models import BookData


class BookForm(forms.ModelForm):

    class Meta:
        model = BookData
        fields = ['name', 'auther_name',
                  'release_year', 'price', 'membership']
