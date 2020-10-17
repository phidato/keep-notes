from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from notes.models import Note
from notes.forms import BookCreateForm
from django.urls import reverse_lazy

# Create your views here.
class NoteCreate(CreateView):
    template_name = 'notes/note_create.html'
    form_class = BookCreateForm


class NoteUpdate(UpdateView):
    template_name = 'notes/note_create.html'
    model = Note
    fields = "__all__"


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')


class NoteListView(ListView):
    model = Note
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context