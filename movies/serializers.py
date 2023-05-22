from rest_framework import serializers
from .models import Movie, Review
class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username',read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','user',)

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source = 'review_set.count',read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user',)
    

class PopularMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class NowPlayingMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'