from django.shortcuts import render
from .models import Publisher, Tag, Genre, Series
from .serializers import PublisherSerializer, SeriesSerializer, TagSerializer, GenreSerializer, serializers
from rest_framework import generics

# Create your views here.

class PublisherList(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetails(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class SeriesList(generics.ListAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer