from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Publisher, Series, Tag, Genre, Language, Season, Episode 


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'Name', 'url']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'Name', 'url']

class LangauageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'Name', 'url']
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'Name', 'url']

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'Name', 'url', 'AgeRating', 'Genres', 'Languages', 'ProducedBy']


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'Name', 'url', 'AgeRating']