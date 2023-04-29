from django import forms
from .models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'description', 'publication_date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BookForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        author = cleaned_data.get('author')
        if author and author != self.user:
            raise forms.ValidationError("Вы не можете добавить книгу от имени другого автора")
        return cleaned_data
