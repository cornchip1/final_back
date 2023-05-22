import requests
import json

API_KEY = 'af9d86a2c68477bba3c90c0d2f29bbf1'

def popular_movies_data():
    popular_movies = []

    for i in range(1,6):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko&page={i}'
        
        movies = requests.get(url).json()
        
        for movie in movies['results']:
            if movie.get('release_date',''):
                fields = {
                    'movie_id':movie['id'],
                    'title':movie['title'],
                    'genre_ids':movie['genre_ids'],
                    'overview':movie['overview'],
                    'poster_path':movie['poster_path'],
                    'release_date':movie['release_date'],
                    'vote_average':movie['vote_average'],                  
                }
                data = {
                    'pk' : movie['id'],
                    'model' : 'movies.movie',
                    'fields' : fields
                }

                popular_movies.append(data)
        
    w = open('movies/fixtures/popular_movies.json','w',encoding='utf-8')
    json.dump(popular_movies, w, indent=4,ensure_ascii=False)

def now_playing_movies_data():
    now_playing_movies = []

    for i in range(1,6):
        url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko&page={i}'
        
        movies = requests.get(url).json()
        
        for movie in movies['results']:
            if movie.get('release_date',''):
                fields = {
                    'movie_id':movie['id'],
                    'title':movie['title'],
                    'genre_ids':movie['genre_ids'],
                    'overview':movie['overview'],
                    'poster_path':movie['poster_path'],
                    'release_date':movie['release_date'],
                    'vote_average':movie['vote_average'],                  
                }
                data = {
                    'pk' : movie['id'],
                    'model' : 'movies.movie',
                    'fields' : fields
                }

                now_playing_movies.append(data)
        
    w = open('movies/fixtures/now_playing_movies.json','w',encoding='utf-8')
    json.dump(now_playing_movies, w, indent=4,ensure_ascii=False)


popular_movies_data()
now_playing_movies_data()
