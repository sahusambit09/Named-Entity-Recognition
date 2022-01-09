from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.Index.as_view(),name="index"),
    path("item/",views.Search.as_view(),name="search"),
    path("med_details/",views.MedDetailView.as_view(),name="meddetail"),
]