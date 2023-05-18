from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    img_url = serializers.ImageField(use_url=True)
    class Meta:
        model = Profile
        fields = '__all__'