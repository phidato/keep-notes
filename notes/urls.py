"""main_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from notes.views import NoteCreate, NoteListView, NoteDetailView, NoteUpdate, NoteDelete

urlpatterns = [
    path('create', NoteCreate.as_view(), name='notecreate'),
    path('', NoteListView.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('update/<int:pk>/', NoteUpdate.as_view(), name='note-update'),
    path('delete/<int:pk>/', NoteDelete.as_view(), name='note-delete'),

]
