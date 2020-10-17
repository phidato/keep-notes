from django import forms
from notes.models import Note

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows':7, 'cols':15}),
        }