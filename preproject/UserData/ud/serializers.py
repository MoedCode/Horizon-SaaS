from rest_framework import serializers
from .models import *
import base64
class UserDataSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, write_only=True)
    class Meta:
        model = UserData
        fields = ['id', 'name', 'email', 'image']
    def create(self, user_data):
         image_file = user_data.pop('image', None)
         user = UserData(**user_data)
         if image_file:
             user.image = image_file.read()
         user.save()
         return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id', 'name', 'email']
