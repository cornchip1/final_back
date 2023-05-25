from rest_framework import serializers
from .models import Actor

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name','img')