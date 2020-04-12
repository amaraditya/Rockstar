from rest_framework import serializers
from .models import movies
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model =User
      fields=('id','username','password')
      extra_kwargs ={'password': {'write_only':True,'required':True}}

   def create(self,validated_data):
      user =User.objects.create_user(**validated_data)
      return user

class moviesSerializer(serializers.ModelSerializer):
   class Meta:
      model =movies
      fields=('id','name',)

