from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from movies.serializers import MovieSerializer, RandomMovieSerializer, MovieListSerializer
from today.serializers import ActorListSerializer
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
    movies = []
    
    for m in range(32):
        movie = get_object_or_404(Movie, pk=choose[m])
        movies.append(movie)
        
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movies_result(request, movie_id):
    API_KEY = 'af9d86a2c68477bba3c90c0d2f29bbf1'
    selected = get_object_or_404(Movie, pk = movie_id).id
    url = f'https://api.themoviedb.org/3/movie/{selected}/similar?api_key={API_KEY}&language=ko'
    data = requests.get(url).json()
    
    ids = list(Movie.objects.values_list('id', flat=True).distinct())
    movie = get_object_or_404(Movie, pk=random.choice(ids))
    if len(data['results']) < 1 :
        serializer = RandomMovieSerializer(movie)
    else:
        start, end = data['page'], data['total_pages']
        if end > 10: end = 10
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
        if len(similar_movies) == 0 : serializer = RandomMovieSerializer(movie)
        else : serializer = RandomMovieSerializer(random.choice(similar_movies))                
    return Response(serializer.data)

@api_view(['GET'])
def random_actors(request):
    ids = list(Actor.objects.values_list('id', flat=True).distinct())
    choose = random.sample(ids, 32)

    actors = []
    for a in range(32):
        actor = get_object_or_404(Actor,pk=choose[a])
        actors.append(actor)
    print('\n\n',actors)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

import ast
@api_view(['GET'])
def actors_result(request, actor_id):
    if request.method == 'GET':
        actor = get_object_or_404(Actor, pk = actor_id)
        filmos = ast.literal_eval(actor.filmos)

        API_KEY = 'af9d86a2c68477bba3c90c0d2f29bbf1'

        choose = random.choice(filmos)
        search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={choose}&language=ko&page=1'
        results = requests.get(search_url).json()
        
        # 검색 결과가 없으면 다른 영화로 재검색
        while len(results['results']) < 1 : 
            choose = random.choice(filmos)
            search_url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={choose}&language=ko&page=1'
            results = requests.get(search_url).json()
        
        # 영화 정보 가져오기
        movie_id = results['results'][0]['id']
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&query={choose}&language=ko'
        data = requests.get(url).json()
        context = {
            'title':data['title'],
            'overview':data['overview'],
            'poster_path':data['poster_path']
        }
        serializer = RandomMovieSerializer(context)
        return Response(serializer.data)