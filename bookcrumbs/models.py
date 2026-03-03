from django.db import models

# Create your models here.
class Book(models.Model):
    image = models.URLField(max_length=250)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    series = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    published_year = models.IntegerField()
    character = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
