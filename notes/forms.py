from django import forms
from notes.models import Note

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'