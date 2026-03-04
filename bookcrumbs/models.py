from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    image = models.URLField(
        max_length=250,
        default="https://images.pexels.com/photos/1333742/pexels-photo-1333742.jpeg",
    )
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    series = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    published_year = models.IntegerField()
    characters = models.CharField(
        max_length=100,
        default="N/A",
    )
    locations = models.CharField(
        max_length=200,
        default="N/A",
    )

    def __str__(self):
        return f"{self.name} by {self.author} | {self.series} | {self.published_year}"
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.id})
