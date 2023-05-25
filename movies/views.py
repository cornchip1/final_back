
from rest_framework.response import Response
from rest_framework.decorators import api_view


# permission Decorators
from rest_framework.decorators import permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewSerializer, MovieSerializer
from .models import Review, Movie

import requests

@api_view(['GET'])
def movie_detail(request, movie_id):
    if request.method == 'GET':
        try: 
            Movie.objects.get(pk = movie_id)
        except Movie.DoesNotExist: 
            API_KEY = 'af9d86a2c68477bba3c90c0d2f29bbf1'
            movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=ko'
            movie = requests.get(movie_url).json()
            credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=ko'
            credit = requests.get(credits_url).json()
            videos_url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=ko'
            video = requests.get(videos_url).json()

            if movie.get('id',''):
                new = Movie.objects.create( 
                    id = movie['id'],
                    movie_id = movie['id'],
                    title = movie['title'],
                    genre_ids = [ movie['genres'][i]['id'] for i in range(len(movie['genres']))] ,
                    overview = movie['overview'],
                    poster_path = movie['poster_path'],
                    release_date = movie['release_date'],
                    vote_average = movie['vote_average'],
                    directors = list(set( crew['name'] for crew in credit['crew'] if crew['known_for_department'] == 'Directing' or crew['department'] == 'Directing')),
                    casts = list(set( cast['name'] for cast in credit['cast'] if cast['known_for_department'] == 'Acting')),
                    video_key = list(result['key'] for result in video['results'] if result['type'] == 'Trailer')  
                    
                )
                new.save()

        movie = get_object_or_404(Movie, pk = movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

# @api_view(['GET'])
# def popular_movies_list(request):
#     if request.method == 'GET':
#         popular_movie = get_list_or_404(Movie.objects.filter(is_popular_movie=True))
#         serializer = PopularMovieListSerializer(popular_movie,many=True)
#         return Response(serializer.data)
    
# @api_view(['GET'])
# def now_playing_movies_list(request):
#     if request.method == 'GET':
#         now_playing_movie = get_list_or_404(Movie.objects.filter(is_now_playing_movie=True))
#         serializer = PopularMovieListSerializer(now_playing_movie,many=True)
#         return Response(serializer.data)
    

# 평점, 한줄리뷰 작성
@api_view(['POST'])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

# 평점, 한줄리뷰 수정, 삭제
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk= review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        if request.user == review.user:
            dic = serializer.data
            dic.update({'is_mine':True})
            return Response(dic)
        else: 
            dic = serializer.data
            dic.update({'is_mine':False})
            return Response(dic)
    elif request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(review, data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else: return Response(status=status.HTTP_406_NOT_ACCEPTABLE)