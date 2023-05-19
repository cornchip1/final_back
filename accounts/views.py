from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import ProfileSerializer


@api_view(['GET','PUT'])
def profile_detail(request,username):
    user = get_object_or_404(User,username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        if request.user.username == username :
            dic = serializer.data
            dic.update({'is_mine':True})
            return Response(dic)
        else: 
            dic = serializer.data
            dic.update({'is_mine':False})
            return Response(dic)
    elif request.method == 'PUT':
        if request.user.username == username :
            serializer = ProfileSerializer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)  
        else: 
            return Response(status =status.HTTP_406_NOT_ACCEPTABLE)