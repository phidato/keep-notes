from django.db import models
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

