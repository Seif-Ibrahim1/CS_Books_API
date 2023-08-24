from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    info = models.TextField(max_length= 1000, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(max_length= 5000, null=True, blank=True)
    publication_year = models.IntegerField(null= True, blank=True)
    authors = models.ManyToManyField(Author, null=True, blank=True, related_name='books')

    def __str__(self):
        return self.name