from rest_framework import serializers
from .models import TodoNote    
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class TodoNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoNote
        fields=['id','title','message']

    