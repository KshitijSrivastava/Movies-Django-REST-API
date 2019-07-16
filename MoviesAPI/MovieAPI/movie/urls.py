from django.contrib import admin
from django.urls import path, include

from movie.views import Home

urlpatterns = [
    path('', Home),
]
