# movies/models.py
from django.db import models
class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    duration = models.IntegerField(help_text="Duración en minutos")
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title