from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# @api_view(['POST'])
# def create_profile(request,user_pk):
#     user = get_object_or_404(User,pk=user_pk)
#     if request.method == 'POST':
#         if request.user == user:
#             serializer = ProfileSerializer(data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save(user = request.user)
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else: 
#             return Response(status =status.HTTP_406_NOT_ACCEPTABLE)
        

# @api_view(['GET','PUT'])
# def profile_detail(request,user_pk,profile_pk):
#     profile = get_object_or_404(Profile,pk=profile_pk)
#     if request.method == 'GET':
#         serializer = ProfileSerializer(profile)
#         print(serializer.data)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         if request.user.pk == user_pk :
#             serializer = ProfileSerializer(profile, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data)  
#         else: 
#             return Response(status =status.HTTP_406_NOT_ACCEPTABLE)