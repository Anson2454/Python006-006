from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movie', views.query_comments),
    path('',views.index)
]