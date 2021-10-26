from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from main.serializers import GenreSerializer, WriterSerializer, BookSerializer
from .models import Genre, Writer, Book

# Create your views here.


# ViewSets define the view behavior.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    search_fields = ('name',)
    ordering_fields = ('writer', 'name', 'genre', 'release_date', 'price')
    filter_fields = ('writer', 'genre')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    serializer_class = BookSerializer
