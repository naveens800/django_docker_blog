from rest_framework import serializers
from .models import Blog, Post, Comment
from django.contrib.auth import get_user_model

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['user', 'title', 'description','created_at','updated_at']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['blog', 'user', 'title', 'content','created_at','updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text','created_at','updated_at']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  
        }
