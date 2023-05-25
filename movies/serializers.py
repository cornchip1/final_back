from rest_framework import serializers
from .models import Movie, Review, Genre

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username',read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','user',)

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','poster_path')

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source = 'review_set.count',read_only=True)
    rate_avg = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    def get_rate_avg(self, instance):
        reviews = instance.review_set.all()
        if len(reviews) > 0 :
            total = 0
            for review in reviews:
                total += review.rate
            rate_avg = total/len(reviews) 
            return round(rate_avg,2)
        else: return 0
    
    def get_genres(self,instance):
        lst = []
        genre_ids = instance.genre_ids[1:-1]
        genre_ids = genre_ids.split(', ')
        for genre in genre_ids:
            lst.append(getattr(Genre.objects.get(pk=genre),'name'))
        return lst

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['review_set']=sorted(response['review_set'], key = lambda x : x['created_at'], reverse=True)
        return response

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user', 'rate_avg',)

class RandomMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview','poster_path')

# class PopularMovieListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'

# class NowPlayingMovieListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'