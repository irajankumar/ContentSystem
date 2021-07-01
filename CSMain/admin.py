from django.contrib import admin
from .models import Tag, Publisher, Series, Genre, Season, Episode, Language
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Series)
admin.site.register(Tag)
admin.site.register(Genre)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Language)