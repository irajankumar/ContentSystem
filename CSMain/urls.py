from django.urls import path
from . import views
from rest_framework import routers



urlpatterns = [
    path('publishers', views.PublisherList.as_view(), name="PubliserList"),
    path('serieses', views.SeriesList.as_view(), name = "SeriesList"),
    path('publishers/<int:pk>', views.PublisherDetails.as_view(), name="PublisherDetails")
]