from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    Name = models.CharField(max_length=255)
    url = models.SlugField(unique=True)
    Logo = models.ImageField(null=True, blank = True)

    def __str__(self) -> str:
        return self.Name

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    Name = models.CharField(max_length=255)
    url = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.Name


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    Name = models.CharField(max_length=255)
    url = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.Name

class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    Name = models.CharField(max_length=20)
    url = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.Name

class Series(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    Name = models.CharField(max_length=255)
    url = models.SlugField(unique=True)
    Carousel = models.ImageField(null = True, blank = True)
    Poster = models.ImageField(null = True, blank = True)
    Description = models.TextField()
    CreatedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='Series_Creators')
    CreatedOn = models.DateTimeField(auto_now_add=True)
    ModifiedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='Series_Modifiers')
    ModifiedOn = models.DateTimeField(auto_now=True)
    DeletedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True, related_name='Series_Deleters')
    DeletedOn = models.DateTimeField(null=True, blank=True, auto_now=False)
    AgeRating = models.PositiveSmallIntegerField()
    Genres = models.ManyToManyField(Genre, db_table='SeriesGenres')
    Tags = models.ManyToManyField(Tag, db_table='SeriesTags')
    Languages = models.ManyToManyField(Language, db_table='SeriesLanguages')
    ProducedBy = models.ForeignKey(Publisher, on_delete= models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.Name

class Season(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    SeasonNumber = models.PositiveSmallIntegerField()
    Name = models.CharField(max_length=255)
    url = models.SlugField(unique=True)
    Carousel = models.ImageField(null = True, blank = True)
    Poster = models.ImageField(null = True, blank = True)
    Description = models.TextField()
    CreatedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='Season_Creators')
    CreatedOn = models.DateTimeField(auto_now_add=True)
    ModifiedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='Season_Modifiers')
    ModifiedOn = models.DateTimeField(auto_now=True)
    DeletedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True, related_name='Season_Deleters')
    DeletedOn = models.DateTimeField(null=True, blank=True, auto_now=False)
    AgeRating = models.PositiveSmallIntegerField()
    Genres = models.ManyToManyField(Genre, db_table='SeasonGenres')
    Tags = models.ManyToManyField(Tag, db_table='SeasonTags')
    Languages = models.ManyToManyField(Language, db_table='SeasonLanguages')
    ParentSeries = models.ForeignKey(Series, on_delete= models.SET_NULL, null=True)


    def __str__(self) -> str:
        return str(self.SeasonNumber) + '-' + self.Name 


class Episode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    EpisodeNumber = models.PositiveSmallIntegerField()
    Name = models.CharField(max_length=255)
    url = models.SlugField(unique=True)
    Carousel = models.ImageField(null = True, blank = True)
    Poster = models.ImageField(null = True, blank = True)
    Description = models.TextField()
    CreatedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='Episode_Creators')
    CreatedOn = models.DateTimeField(auto_now_add=True)
    ModifiedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, related_name='Episode_Modifiers')
    ModifiedOn = models.DateTimeField(auto_now=True)
    DeletedBy = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True, related_name='Episode_Deleters')
    DeletedOn = models.DateTimeField(null=True, blank=True, auto_now=False)
    AgeRating = models.PositiveSmallIntegerField()
    Genres = models.ManyToManyField(Genre, db_table='EpisodeGenres')
    Tags = models.ManyToManyField(Tag, db_table='EpisodeTags')
    Languages = models.ManyToManyField(Language, db_table='EpisodeLanguages')
    ParentSeason = models.ForeignKey(Season, on_delete= models.SET_NULL, null=True)
    isFree = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.EpisodeNumber) + '-' + self.Name