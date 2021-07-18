from django.urls import path
from . import views
from rest_framework import routers



urlpatterns = [
    path('languages', views.LangauageList.as_view(), name = 'LanguageList'),
    path('languages/<uuid:pk>', views.LanguageDetails.as_view(), name = 'LanguageDetails'),
    path('genres', views.GenreList.as_view(), name = 'GenreList'),
    path('genres/<uuid:pk>', views.GenreDetails.as_view(), name = 'GenreDetails'),
    path('tags', views.TagList.as_view(), name = 'TagList'),
    path('tags/<uuid:pk>', views.TagDetails.as_view(), name = 'TagDetails'),
    path('publishers', views.PublisherList.as_view(), name="PubliserList"),
    path('publishers/<uuid:pk>', views.PublisherDetails.as_view(), name="PublisherDetails"),
    path('serieses', views.SeriesList.as_view(), name = "SeriesList"),
    path('serieses/<uuid:pk>', views.seriesDetails.as_view(), name = "SeriesDetails"),
]