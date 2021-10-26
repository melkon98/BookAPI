from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")
    name = models.CharField(max_length=50)
    synopsis = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")
    release_date = models.DateField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.name