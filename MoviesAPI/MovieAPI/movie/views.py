from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import json


from movie.serializers import MovieSerializer
from movie.models import Movie
# Create your views here.

class PaginationMovie(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


def Home(request):
    return HttpResponse("Hello world!")

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieList(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PaginationMovie

@api_view(['GET'])
def movie_delete(request):
    movie_name = request.GET.get('movie_name', None)
    year = request.GET.get('year', None)

    if movie_name and year:
        movie_objects = Movie.objects.filter(movie_name = movie_name).filter(year = year)
    elif movie_name and year is None:
        movie_objects = Movie.objects.filter(movie_name = movie_name)
    elif movie_name is None and year:
        movie_objects = Movie.objects.filter(year = year)
    else:
        return Response("No Movie Data Deleted", status=status.HTTP_201_CREATED)

    if len(movie_objects) == 0:
        return Response("No Movie Data Deleted", status=status.HTTP_201_CREATED)
    else:
        print(movie_objects)
        serializer = MovieSerializer(movie_objects, many=True)
        print(serializer)
        movie_objects.delete()
        return Response("Movies Deleted from database", status=status.HTTP_201_CREATED)

@api_view(['POST'])
def movie_insert_list(request):
    data = request.POST.get('list')
    final_data = eval(data)
    for obj in final_data:
        Movie.objects.create(movie_name=obj['movie_name'], year=obj['year'])
    return Response("List of Movies Added from database", status=status.HTTP_201_CREATED)
