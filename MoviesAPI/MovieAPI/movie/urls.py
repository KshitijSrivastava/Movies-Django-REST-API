from django.contrib import admin
from django.urls import path, include

from movie.views import Home, movie_list, MovieList

urlpatterns = [
    path('', Home),
    path('movie/', MovieList.as_view()),
]
