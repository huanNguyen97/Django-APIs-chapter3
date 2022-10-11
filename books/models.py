from django.db import models


class Book(models.Model):
  title = models.CharField(max_length=250)
  subtitle = models.CharField(max_length=250)
  author = models.CharField(max_length=100)
  isbn = models.CharField(max_length=13)

  # Return default value of Book model.
  def __str__(self):
    return self.title
