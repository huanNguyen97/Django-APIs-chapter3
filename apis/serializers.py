from dataclasses import field
from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):

  # Serializers model used for converting class model to Json
  class Meta:
    model = Book
    fields = ("title", "subtitle", "author", "isbn")
