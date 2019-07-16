from django.contrib import admin
from django.urls import path, include

from movie.views import Home, movie_list, MovieList, movie_delete, movie_insert_list

urlpatterns = [
    path('', Home),
    path('movie/', MovieList.as_view()),
    path('movie-delete/', movie_delete),
    path('movielist_add/', movie_insert_list),
]
