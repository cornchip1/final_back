
from rest_framework.response import Response
from rest_framework.decorators import api_view


# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewSerializer, MovieSerializer
from .models import Review, Movie

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

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