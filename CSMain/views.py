from django.shortcuts import render
from django.utils.translation import check_for_language
from .models import Language, Publisher, Tag, Genre, Series
from .serializers import LangauageSerializer, PublisherSerializer, SeriesSerializer, TagSerializer, GenreSerializer, serializers
from rest_framework import generics

# Create your views here.

class LangauageList(generics.ListAPIView):
    queryset = Language.objects.all().order_by('Name')
    serializer_class = LangauageSerializer

class LanguageDetails(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LangauageSerializer

class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all().order_by('Name')
    serializer_class = GenreSerializer

class GenreDetails(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('Name')
    serializer_class = TagSerializer

class TagDetails(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PublisherList(generics.ListAPIView):
    queryset = Publisher.objects.all().order_by('Name')
    serializer_class = PublisherSerializer

class PublisherDetails(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class SeriesList(generics.ListAPIView):
    queryset = Series.objects.all().order_by('-CreatedOn')
    serializer_class = SeriesSerializer

class seriesDetails(generics.RetrieveAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer