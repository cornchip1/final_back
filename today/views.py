from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from movies.serializers import MovieSerializer, RandomMovieSerializer
from movies.models import Review, Movie
from today.models import Actor

import requests, random

# Create your views here.
@api_view(['GET'])
def random_movie(request):
    movies = get_list_or_404(Movie)
    ids = Movie.objects.values_list('id', flat=True).distinct()
    x = random.randrange(1,len(movies))
    movie = get_object_or_404(Movie, pk=ids[x])
    serializer =MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def random_movies(request):
    ids = list(Movie.objects.values_list('id', flat=True).distinct())
    choose = random.sample(ids, 32)
    return Response(choose)

@api_view(['GET'])
def movies_result(request, movie_id):
    API_KEY = 'af9d86a2c68477bba3c90c0d2f29bbf1'
    selected = get_object_or_404(Movie, pk = movie_id).id
    url = f'https://api.themoviedb.org/3/movie/{selected}/similar?api_key={API_KEY}&language=ko'
    data = requests.get(url).json()
    
    start, end = data['page'], data['total_pages']
    similar_movies = []

    for page in range(start,end):
        page_url = f'{url}&page={page}'
        d = requests.get(page_url).json() # 각 page 에 있는 data
        for result in d['results']:
            if result['vote_average'] >= 8.0 and result['vote_count'] >= 1000 and result['adult'] == False:
                context = {
                    'title':result['title'],
                    'overview':result['overview'],
                    'poster_path':result['poster_path'],
                }
                similar_movies.append(context)
    serializer = RandomMovieSerializer(random.choice(similar_movies))        
    # print(random.choice(similar_movies))                      
    return Response(serializer.data)

@api_view(['GET'])
def random_actors(request):
    ids = list(Actor.objects.values_list('id', flat=True).distinct())
    choose = random.sample(ids, 32)
    return Response(choose)

import ast
# 배우가 출연한 영화 중 1개 골라서 보여주기 -> search result 의 첫번째 값 보여주기
@api_view(['GET'])
def actors_result(request, actor_id):
    actor = get_object_or_404(Actor, pk = actor_id)
    filmos = ast.literal_eval(actor.filmos)

    API_KEY = 'af9d86a2c68477bba3c90c0d2f29bbf1'

    choose = random.choice(filmos)
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={choose}&language=en-US&page=1'
    results = requests.get(search_url).json()
    
    while len(results['results']) < 1 : 
        # print('***************\n','결과 없음')
        choose = random.choice(filmos)
        search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={choose}&language=en-US&page=1'
        results = requests.get(search_url).json()
    
    movie_id = results['results'][0]['id']
    # print('************\n결과\n', results['results'][0])

    url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={API_KEY}&language=ko'
    data = requests.get(url).json()
    similar_movies = []

    if len(data['results']) < 1 :
        # print('*****\n예외처리\n')
        ids = list(Movie.objects.values_list('id', flat=True).distinct())
        exception_handling = random.choice(ids)
        movie = get_object_or_404(Movie,pk=exception_handling)
        context = {
            'title':movie.title,
            'overview':movie.overview,
            'poster_path':movie.poster_path
        }
        serializer = RandomMovieSerializer(context)
    else:
        start, end = data['page'], data['total_pages']
        if end > 10 : end = 10
        for page in range(start,end+1):
            page_url = f'{url}&page={page}'
            d = requests.get(page_url).json() # 각 page 에 있는 data
            for result in d['results']:
                if result.get('vote_average',''):
                    if result['vote_average'] >= 8.0 and result['vote_count'] >= 1000 and result['adult'] == False:
                        context = {
                            'title':result['title'],
                            'overview':result['overview'],
                            'poster_path':result['poster_path'],
                        }
                        similar_movies.append(context)
    # print('\n\n',similar_movies)
              

    if len(similar_movies) == 0 :
        # print('*****\n 조건에 맞는 비슷한 영화가 없는 예외처리\n')
        ids = list(Movie.objects.values_list('id', flat=True).distinct())
        exception_handling = random.choice(ids)
        movie = get_object_or_404(Movie,pk=exception_handling)
        context = {
            'title':movie.title,
            'overview':movie.overview,
            'poster_path':movie.poster_path
        }
        serializer = RandomMovieSerializer(context)
    else: serializer = RandomMovieSerializer(random.choice(similar_movies)) 
             
    # print(random.choice(similar_movies))                      
    return Response(serializer.data) 


