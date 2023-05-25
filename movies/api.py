import requests
import json

API_KEY = 'af9d86a2c68477bba3c90c0d2f29bbf1'

def popular_movies_data():
    popular_movies = []

    for i in range(1,6):
        movies_url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko&page={i}'
        movies = requests.get(movies_url).json()
        
        for movie in movies['results']:
            if movie.get('release_date',''):
                movie_id = movie['id']
                credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=ko'
                credit = requests.get(credits_url).json()
                videos_url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=ko'
                video = requests.get(videos_url).json()

                fields = {
                    'movie_id':movie['id'],
                    'title':movie['title'],
                    'genre_ids':movie['genre_ids'],
                    'overview':movie['overview'],
                    'poster_path':movie['poster_path'],
                    'release_date':movie['release_date'],
                    'vote_average':movie['vote_average'],
                    'directors' : list(set( crew['name'] for crew in credit['crew'] if crew['known_for_department'] == 'Directing' or crew['department'] == 'Directing')),
                    'casts':  list(set(cast['name'] for cast in credit['cast'] if cast['known_for_department'] == 'Acting')),
                    'video_key':  list(result['key'] for result in video['results'] if result['type'] == 'Trailer')
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
        movies_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko&page={i}'
        movies = requests.get(movies_url).json()

        for movie in movies['results']:
            movie_id = movie['id']
            credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=ko'
            credit = requests.get(credits_url).json()
            videos_url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=ko'
            video = requests.get(videos_url).json()
            
            if movie.get('release_date',''):
                fields = {
                    'movie_id':movie['id'],
                    'title':movie['title'],
                    'genre_ids':movie['genre_ids'],
                    'overview':movie['overview'],
                    'poster_path':movie['poster_path'],
                    'release_date':movie['release_date'],
                    'vote_average':movie['vote_average'],
                    'directors' : list(set( crew['name'] for crew in credit['crew'] if crew['known_for_department'] == 'Directing' or crew['department'] == 'Directing')),
                    'casts':  list(set( cast['name'] for cast in credit['cast'] if cast['known_for_department'] == 'Acting'  )),
                    'video_key':  list(result['key'] for result in video['results'] if result['type'] == 'Trailer')      
        
                }
                data = {
                    'pk' : movie['id'],
                    'model' : 'movies.movie',
                    'fields' : fields
                }

                now_playing_movies.append(data)
        
    w = open('movies/fixtures/now_playing_movies.json','w',encoding='utf-8')
    json.dump(now_playing_movies, w, indent=4,ensure_ascii=False)

def genres_data():
    genres_lst = []
    genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko'
    genres = requests.get(genres_url).json()

    for genre in genres['genres']:
        print(genre['id'])
        fields = {
            'genre_id' : genre['id'],
            'name' : genre['name'],
        }
        data = {
            'pk' : int(genre['id']),
            'model': 'movies.genre',
            'fields':fields
        }
        genres_lst.append(data)

    w = open('movies/fixtures/genres.json','w',encoding='utf-8')
    json.dump(genres_lst, w, indent=4,ensure_ascii=False)

popular_movies_data()
now_playing_movies_data()
# genres_data()
