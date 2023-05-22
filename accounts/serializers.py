from rest_framework import serializers
from .models import User
from community.serializers import ArticleSerializer,CommentSerializer

from rest_framework import serializers

from community.serializers import CommentSerializer, ArticleSerializer, ArticleListSerializer
from community.models import Article, Comment
from movies.serializers import ReviewSerializer

class ProfileSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    articles_count = serializers.IntegerField(source = 'articles.count', read_only = True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source = 'comments.count', read_only = True)
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source = 'reviews.count', read_only = True)
    
    class Meta:
        model = User
        fields = ('username','date_joined','img','background_img','articles','articles_count','comments','comments_count', 'reviews', 'reviews_count')
        # fields = '__all__'
        read_only_fields = ('username',)
    