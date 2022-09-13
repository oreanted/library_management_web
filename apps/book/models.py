from django.db import models


# Create your models here.

class BookData(models.Model):
    name = models.CharField(max_length=40)
    auther_name = models.CharField(max_length=40)
    release_year = models.CharField(max_length=5)
    price = models.IntegerField()
    TECHNOLOGY_GENRE = "Technology"
    RELIGION_GENRE = "Religion"
    SCIENCE_GENRE = "Science & Research"
    POLITICS_LAWS_GENRE = 'Politics & Laws'
    LIFESTYLE_GENRE = 'Lifestyle'
    FICTION_GENRE = 'Fiction & Literature'
    GENRE_CHOICES = [
        (TECHNOLOGY_GENRE, "Technology"),
        (RELIGION_GENRE, "Religion"),
        (SCIENCE_GENRE, "Science & Research"),
        (POLITICS_LAWS_GENRE, 'Politics & Laws'),
        (LIFESTYLE_GENRE, 'Lifestyle'),
        (FICTION_GENRE, 'Fiction & Literature'),
    ]
    membership = models.CharField(max_length=100, choices=GENRE_CHOICES, default=TECHNOLOGY_GENRE)
