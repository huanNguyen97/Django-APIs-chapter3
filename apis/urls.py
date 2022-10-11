from nturl2path import url2pathname
from django.urls import path

from .views import BookAPIView


urlpatterns = [
  path("", BookAPIView.as_view(), name="book_list"),
]

