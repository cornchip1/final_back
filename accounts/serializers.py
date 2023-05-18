from rest_framework import serializers
# from .models import Profile

from rest_framework import serializers

from community.serializers import CommentSerializer, ArticleSerializer, ArticleListSerializer


# class ProfileSerializer(serializers.ModelSerializer):
#     # article_set = ArticleSerializer(many=True, read_only=True)
#     # article_count = serializers.IntegerField(source = 'article_set.count',read_only=True)

#     class Meta:
#         model = Profile
#         fields = '__all__'
